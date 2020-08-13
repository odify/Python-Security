from __future__ import print_function
import os
## import logging



import netfilterqueue as nfq

from packets import IPPacket, TCPPacket, to_tuple

_NFQ_INIT = 'iptables -I INPUT -j NFQUEUE --queue-num %d'
_NFQ_CLOSE = 'iptables -D INPUT -j NFQUEUE --queue-num %d'
_pipe = None




def get_pipe():
    """This function returns the query pipe for TCP connection state.
    Sadly, this breaks some modularity with rule classes.  However, it is a
    quick fix for the one rule (TCPStateRule) that needs access to TCP
    conenction state.
    """
    global _pipe
    return _pipe


class PyWall(object):
    def __init__(self, tcp_queue, query_pipe, queue_num=1, default='DROP'):
        global _pipe
        _pipe = query_pipe
        self.queue_num = queue_num
        self.tcp_queue = tcp_queue
        self.query_pipe = query_pipe
        self.chains = {'INPUT': [], 'ACCEPT': None, 'DROP': None}
        self.default = default
        self._start = 'INPUT'
        self._old_handler = None



    def add_chain(self, chain_name):
        self.chains[chain_name] = []

    def add_brick(self, chain, rule):
        self.chains[chain].append(rule)

    def _apply_chain(self, chain, nfqueue_packet, pywall_packet):

        l = logging.getLogger('pywall.pywall')
        if chain == 'ACCEPT':
            payload = pywall_packet.get_payload()

            l.debug('ACCEPT %s' % unicode(pywall_packet))
            if type(payload) is TCPPacket:
                tup = to_tuple(pywall_packet)
                if self.tcp_queue is not None:
                    self.tcp_queue.put((tup, bool(payload.flag_syn),
                                        bool(payload.flag_ack),
                                        bool(payload.flag_fin)))
            nfqueue_packet.accept()
        elif chain == 'DROP':
            l.info('DROP %s' % unicode(pywall_packet))
            nfqueue_packet.drop()
        else:
            for rule in self.chains[chain]:
                result = rule(pywall_packet)
                if result:
                    return self._apply_chain(result, nfqueue_packet,
                                             pywall_packet)
            return self._apply_chain(self.default, nfqueue_packet,
                                     pywall_packet)

    def callback(self, packet):
        pywall_packet = IPPacket(packet.get_payload())
        self._apply_chain(self._start, packet, pywall_packet)

    def erect(self, **kwargs):
        """Run the PyWall!"""
        setup = _NFQ_INIT % self.queue_num
        os.system(setup)
        print('Set up IPTables: ' + setup)

        nfqueue = nfq.NetfilterQueue()
        nfqueue.bind(self.queue_num, self.callback)
        if kwargs.get('test', False):
            lock = kwargs.get('lock', None)
            if lock:
                lock.release()

        try:
            nfqueue.run()
        except KeyboardInterrupt:
            pass
        finally:


            # Always remove the firewall rule!

            teardown = _NFQ_CLOSE % self.queue_num
            os.system(teardown)
            print('\nTore down IPTables: ' + teardown)

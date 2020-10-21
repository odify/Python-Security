#!/usr/bin/env python3


import socket
from tabulate import tabulate
import os
import datetime
import pyfiglet


result = pyfiglet.figlet_format("HOST INFOS CLI")
print(result)
#print("\n") # describtion-row
os.system("date")
print("-----------------------")


class Network_Information(object):   

    def __init__(self, url="www.github.com"):
        self.url = url
        self.host_name = socket.gethostname()
        self.ip_adress = socket.gethostbyname(self.host_name)
        self.remote_ip = self.remote_info()




    def __repr__(self):
        data = {"Host Name:": [self.host_name],
                  "IP:": [self.ip_adress],
                f"{self.url}:": [self.remote_ip]}
        table = tabulate(data, headers="keys", tablefmt="grid")
        return table


    def remote_info(self):
        try:
            return socket.gethostbyname(self.url)
        except socket.error as err_msg:
            return err_msg
if __name__ == "__main__":
    print(Network_Information())                    




#!/usr/bin/env python3

import os
import datetime
#import pyfiglet
import random
from subprocess import PIPE, Popen


# MAIN FUNCTION 1


def cret(command):
    process = Popen(
        args=command,
        stdout=PIPE,
        shell=True
    )
    return process.communicate()[0]


# MAIN FUNCTION 2


def randmac():
    return [0x00, 0x16, 0x3e,
            random.randint(0x00, 0x7f),
            random.randint(0x00, 0xff),
            random.randint(0x00, 0xff)]


def retrandmac(mac):
    return ':'.join(map(lambda x: "%02x" % x, mac))




print("                                             -----------------------")
print("                                              MAC ID CHANGER  V.0.1 ")
print("                                             -----------------------")
os.system("date")


infname = cret('ifconfig -a  | egrep "^[wl-wl]+" | sed "s/: .*//" | grep -v "lo"')
infname = infname[:6]
infname = infname.decode('utf-8')



cmdgetmac = ('cat /sys/class/net/' + infname + '/address')
crrntmac = cret("cat /sys/class/net/" + infname + "/address")
crrntmac = crrntmac.decode('utf-8')
print(
    "YOUR CURRENT MAC ID = " + crrntmac + "\nOPTIONS:\n1. MANUALLY \n2. RANDOMLY")
opt = int(input())

if opt == 1:
    print("Please Enter Your New MAC address: \ne.g 44:a3:e2:0b:4a:30")

    newmac = input()
    print(".......LOADING........")

    #OFFLINE
    cret('nmcli radio wifi off')

    changemaccmd = "sudo ip link set dev " + infname + " address " + newmac

    # REBUILING

    cret(changemaccmd)

    # ONLINE
    cret('nmcli radio wifi on')
    cr = cret("cat /sys/class/net/" + infname + "/address")
    cr = cr.decode('utf-8')

    print("\nNow Your Current mac address = " + cr)




elif opt == 2:
    genmac = retrandmac(randmac())
    print(".......LOADING........")
    cret('nmcli radio wifi off')
    changemaccmd = "sudo ip link set dev " + infname + " ADRESS " + genmac
    cret(changemaccmd)
    cret('nmcli radio wifi on')
    cr = cret("cat /sys/class/net/" + infname + "/address")
    cr = cr.decode('utf-8')
    print("NEW MAC ID = " + cr)


else:
    print("failed! Ask your admins for permission")


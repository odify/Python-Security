#!/usr/bin/env python3

import random
from subprocess import PIPE, Popen


def cret(command):
    process = Popen(
        args=command,
        stdout=PIPE,
        shell=True
    )
    return process.communicate()[0]


def randmac():
    return [0x00, 0x16, 0x3e,
            random.randint(0x00, 0x7f),
            random.randint(0x00, 0xff),
            random.randint(0x00, 0xff)]


def retrandmac(mac):
    return ':'.join(map(lambda x: "%02x" % x, mac))


print("                                             +-+-+-+ +-+-+-+-+-+-+-+")
print("                                             |M|A|C| |c|h|a|n|g|e|r|")
print("                                             +-+-+-+ +-+-+-+-+-+-+-+")

infname = cret('ifconfig -a  | egrep "^[wl-wl]+" | sed "s/: .*//" | grep -v "lo"')

infname = infname[:6]
infname = infname.decode('utf-8')
cmdgetmac = ('cat /sys/class/net/' + infname + '/address')
crrntmac = cret("cat /sys/class/net/" + infname + "/address")
crrntmac = crrntmac.decode('utf-8')
print(
    "Your mac address = " + crrntmac + "\nEnter Option:\n1. Enter MAC manually \n2. Random MAC")
opt = int(input())

if opt == 1:
    print("Enter Your New MAC address: \nExmple:  46:d2:f4:0c:2a:50")

    newmac = input()
    print("Please wait changing  mac address..................")

    cret('nmcli radio wifi off')

    changemaccmd = "sudo ip link set dev " + infname + " address " + newmac
    cret(changemaccmd)
    # turning on wifi
    cret('nmcli radio wifi on')
    # PATH 4 MAC
    cr = cret("cat /sys/class/net/" + infname + "/address")
    cr = cr.decode('utf-8')

    print("\nNow Your Current mac address = " + cr)



elif opt == 2:
    genmac = retrandmac(randmac())
    print("Please wait generating new mac address.....................")
    cret('nmcli radio wifi off')
    changemaccmd = "sudo ip link set dev " + infname + " address " + genmac
    cret(changemaccmd)
    cret('nmcli radio wifi on')
    cr = cret("cat /sys/class/net/" + infname + "/address")
    cr = cr.decode('utf-8')
    print("Now Your Current mac address = " + cr)

else:
    print("You Have Selected wrong Option")

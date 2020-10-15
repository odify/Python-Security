import os
import subprocess
import time


print(" START CLEANING DNS ")


os.system("sudo /etc/init.d/dns-clean start")
time.sleep(60)
os.system("sudo /etc/init.d/dns-clean start")
time.sleep(3000)
os.system("sudo /etc/init.d/dns-clean start")
time.sleep(6000)
os.system("sudo /etc/init.d/dns-clean start")
time.sleep(18000)
os.system("sudo /etc/init.d/dns-clean start")
time.sleep(6000)
os.system("sudo /etc/init.d/dns-clean start")
time.sleep(3000)


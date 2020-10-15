import os
import time
import datetime

time.sleep(1)

os.system("date")

time.sleep(2)

os.system("sudo apt-get autoremove")

time.sleep(3)

os.system("sudo /etc/init.d/dns-clean start")

time.sleep(4)

os.system("sudo apt-get clean && sudo apt-get autoclean")

time.sleep(3)

os.system("sudo /etc/init.d/dns-clean start")

time.sleep(2)

os.system("sudo apt-get autoremove")


#????


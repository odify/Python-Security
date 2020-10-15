#!/usr/bin/env python3



import sys
import os
import threading
import socket
from datetime import datetime


from queue import Queue



print_lock = threading.Lock()


# os.system("sudo /etc/init.d/dns-clean start")
#time.sleep(10)


host = input("REMOTE HOST: ")


ip = socket.gethostbyname(host)



print("-" * xx(port))


print("              LOADING --------> ", ip)


print("-" * yy(port))





t1 = datetime.now()

def scan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((ip, port))
        if result == 0:
            print("\n Port %d OPEN" %(port))
            sock.close()
        else:
            print("\n Port %d LOCKED " %(port))
            
    except:
        pass





def threader():
    while True:
        worker = q.get()

        scan(worker)

        q.task_done()



q = Queue()

for x in range(60):
     t = threading.Thread(target=threader)

     t.daemon = True

     t.start()


for worker in range(1,100):
    q.put(worker)

# wait until the thread terminates.
q.join()

## Checking the time again
t2 = datetime.now()
## Calculates the difference of time, to see how long it took to run the script
total = t2 - t1
## Printing the information to screen
print('Scanning Completed in: ', total)

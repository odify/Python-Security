import sys


## IP range address generator
## 192.168.1.1 --2- 192.168.2.255


def help():
    print usage


def generate(start, stop, logfile):
    for d in range(int(start[3]), int(stop[3]) + 1):
        for c in range(int(start[2]), int(stop[2]) + 1):
            for b in range(int(start[1]), int(stop[1]) + 1):
                for a in range(int(start[0]), int(stop[0]) + 1):
                    res = "{}.{}.{}.{}".format(a, b, c, d)
                    if logfile:
                        logfile.writelines("{}\n".format(res))
    return

if __name__ == "__main__":

    f = open("ip_list.log", "w+")

    if len(sys.argv) != 3:
        help()
        exit(0)




    start = sys.argv[1].split(".")
    stop = sys.argv[2].split(".")
    print "\n[+] generating IP addresses in range from {} to {}...".format(sys.argv[1], sys.argv[2])
    generate(start, stop, f)
    print "[+] addresses generated...\n"

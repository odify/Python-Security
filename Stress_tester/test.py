#!/usr/bin/env python3


import random
import time
import multiprocessing
from multiprocessing import Process

Logical_cores = multiprocessing.cpu_count()
Pros = []

def work():
    zero = list()
    while True:
        one = float()
        two = float()
        three = float()
        four = float()

        one = random.random()
        two = random.random()
        three = random.random()
        four = random.random()


        five = one * two
        six = three * four


        zero.append(five + six)
        zero.append(five - six)
        zero.append(five * six)
        zero.append(five / six)


if __name__ == '__main__':

    for x in range(Logical_cores):
        p = Process(target=work)
        time.sleep(3)
        Pros.append(p)
        p.start()


for t in Pros:

    t.join()


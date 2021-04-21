# This file is created for giving one example to print odd even number till a specific range using 2 independent threads

Below code is written for printing odd and even number independently using two different threads

Program:

import threading
import time

num = int(input())  # input passed 20, for printing 1-20 using
ls = []

def odd(num):
    for i in range(1, num + 1):
        if i % 2 == 1:
            ls.append(i)
            time.sleep(0.02)

def even(num):
    for j in range(1,num+1):
        if j % 2 == 0:
            ls.append(j)
            time.sleep(0.02)

x = threading.Thread(target = odd, args=(num,))
x.start()

y = threading.Thread(target = even, args=(num,))
y.start()

x.join()
y.join()

for k in range(len(ls)):
    print(ls[k], end = " ")



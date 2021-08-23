# This file is created for giving one example to print odd even number till a specific range using 2 independent threads
Program -
------------------------------------------------------------------------------------------------------------------------
import threading
import time

num = int(input())  # input passed 20, for printing 1-20 using below separate threads
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

Output :
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
Explantion - 1,3,5,7 and so on... printed using first thread
             2,4,6,8 and so on... printed using second thread

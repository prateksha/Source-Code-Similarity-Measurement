#!/bin/python3

import sys


N = int(input().strip())

if (N % 2 != 0):
    print ("Weird")
elif (N % 2 == 0 and N >= 2 and N <= 5):
    print ("Not Weird")
elif (N % 2 == 0 and N > 5 and N <= 20):
    print ("Weird")
#elif (N % 2 == 0 && N > 20):
else:
    print ("Not Weird")

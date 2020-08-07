#!/bin/python3

import sys


N = int(input().strip())
if (N%2 == 0):
    if (6<=N<=20):
        print ("Weird")
    else:
        print ("Not Weird")
else:
    print ("Weird")
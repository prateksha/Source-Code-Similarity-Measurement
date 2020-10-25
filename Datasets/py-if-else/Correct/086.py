#!/bin/python3

import sys


N = int(input().strip())
if N%2 == 1: print ("Weird") 
else: 
    if N <= 5: print ("Not Weird")
    elif N <= 20: print ("Weird")
    else: print ("Not Weird")
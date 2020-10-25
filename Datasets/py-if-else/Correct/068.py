#!/bin/python3

import sys


N = int(input().strip())

if((N >= 2 and N<=5) and ((N%2) == 0)):
    print("Not Weird")
elif(N >= 21 and ((N%2) == 0)):
    print("Not Weird")    
else:
    print("Weird")

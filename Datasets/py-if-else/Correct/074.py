#!/bin/python3

import sys


N = int(input().strip())
if not(N%2==0): 
    print("Weird")
elif N<5: 
    print("Not Weird")
elif N<21:
    print("Weird")
else: 
    print("Not Weird")

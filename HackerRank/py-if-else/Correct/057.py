#!/bin/python3
import sys

N = int(input().strip())
if((N % 2 == 0 and (N >= 2 and N <= 5)) or (N % 2 == 0 and (N > 20))):
    print("Not Weird")
else:
    print("Weird")
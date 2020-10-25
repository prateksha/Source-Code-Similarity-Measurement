#!/bin/python3

import sys

N = int(input().strip())
even = (N % 2 == 0)
if(not even or (N >= 6 and N <= 20)):
    print("Weird")
elif(even and ((N >= 2 and N <= 6) or N > 20)):
    print("Not Weird")
    
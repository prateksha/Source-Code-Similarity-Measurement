#!/bin/python3

import sys
N = int(input().strip())
if N % 2 != 0:
    print("Weird")
else:
    if N > 1 and N < 6:
        print("Not Weird")
    elif N > 6 and N < 21:
        print("Weird")
    elif N > 20:
        print("Not Weird")
    
#!/bin/python3

import sys


n = int(input().strip())

if n % 2 == 1:
    print("Weird")
else:
    if n >= 6 and n <= 20:
        print("Weird")
    else:
        print("Not Weird")
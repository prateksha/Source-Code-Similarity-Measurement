#!/bin/python3

import sys


n = int(input().strip())
if n % 2 == 0:
    if 2 <= n <= 5:
        print("Not Weird")
    elif 6 <= n <= 20:
        print("Weird")
    elif n > 20:
        print("Not Weird")
else:
    print("Weird")
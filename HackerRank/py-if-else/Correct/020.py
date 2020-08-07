#!/bin/python3

import sys

n = int(input().strip())

# odd (any) or even (6 to 20)

if n%2 == 0:
    if n >= 6 and n <= 20:
        print("Weird")
    else:
        print("Not Weird")
else:
    print("Weird")
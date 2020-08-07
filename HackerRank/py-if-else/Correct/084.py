#!/bin/python3

import sys


n = int(input().strip())


if n%2 != 0:
    print ("Weird")
elif n >= 6 and n<=20:
    print ("Weird")
else:
    print ("Not Weird")

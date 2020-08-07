#!/bin/python3

import sys


N = int(input().strip())
weird = 'Weird'
not_weird = 'Not Weird'

if N % 2 != 0:
    print(weird)
elif N >= 2 and N <= 5 and N % 2 == 0:
    print(not_weird)
elif N >= 6 and N <= 20 and N % 2 == 0:
    print(weird)
elif N >= 20 and N % 2 == 0:
    print(not_weird)
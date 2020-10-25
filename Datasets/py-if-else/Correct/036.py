#!/bin/python3

import sys


N = int(input().strip())

if not N % 2 and (N < 6 or N > 20):
    print('Not Weird')
else:
    print('Weird')
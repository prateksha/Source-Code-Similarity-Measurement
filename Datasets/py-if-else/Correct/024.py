#!/bin/python3

import sys


N = int(input().strip())

if (N % 2 == 1):
    print('Weird')
else:
    if (N < 6):
        print('Not Weird')
    elif (N > 20):
        print('Not Weird')
    else:
        print('Weird')
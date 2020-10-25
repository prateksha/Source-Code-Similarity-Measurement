#!/bin/python3

import sys


N = int(input().strip())

if not(N % 2 == 0):
    print('Weird')
elif N % 2 == 0:
    if N in range(2,6):
        print('Not Weird')
    elif N in range(6,21):
        print('Weird')
    elif N > 20:
        print('Not Weird')
    

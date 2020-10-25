#!/bin/python3

import sys


N = int(input())
if N%2==1:
    print('Weird')
else:
    if N in range(2,6) or N>20:
        print('Not Weird')
    elif N in range(6,21):
        print('Weird')
        
    
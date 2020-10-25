#!/bin/python3

import sys
N = int(input().strip())
if N%2==1:
    print('Weird')
elif N>20:
    print('Not Weird')
elif N>5:
    print('Weird')
elif N>1:
    print('Not Weird')
    

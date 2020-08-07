#!/bin/python3

import sys


N = int(input().strip())
print('Weird' if N % 2 == 1 or 6 <= N <= 20 else 'Not Weird')
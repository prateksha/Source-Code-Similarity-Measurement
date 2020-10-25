#!/bin/python3

import sys


N = int(input().strip())

if N % 2 == 1:
    print("Weird")

if 2 <= N <= 5 and N % 2 == 0: 
    print("Not Weird")
if N % 2 == 0 and 6 <= N <= 20:
    print("Weird")
if N > 20 and N % 2 == 0:
    print("Not Weird")

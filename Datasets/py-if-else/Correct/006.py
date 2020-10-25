#!/bin/python3

import sys


N = int(input().strip())
res = "Weird"

if N%2 == 0:
    if N<= 5 or N > 20:
        res = "Not Weird"
        
print(res)
    

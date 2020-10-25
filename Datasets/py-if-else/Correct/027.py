#!/bin/python3

import sys


n = int(input().strip())
if (n>20):
    if(n%2==0):
        print("Not Weird")
    else:
        print("Weird")
        
else:
    if(n%2==0):
        if n in range(2,6):
            print("Not Weird")
        else:
            print("Weird")
    else:
        print("Weird")
            

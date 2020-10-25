#!/bin/python3

import sys


N = int(input().strip())
x=N%2
if (x!=0):
    print("Weird")
elif (x==0):
    if (N>=2 and N<=5):
        print("Not Weird")
    if(N>=6 and N<=20):
         print("Weird")
    elif(N>20): 
         print("Not Weird")
        
    
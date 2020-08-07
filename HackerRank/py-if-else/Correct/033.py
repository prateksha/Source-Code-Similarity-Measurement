#!/bin/python3

import sys


N = int(input().strip())

if(N % 2 == 1):{
   print("Weird")
    }
elif(N < 6):
    {
    print("Not Weird")
    }
elif(N< 21):
    {
        print ("Weird")
    }
else: print("Not Weird")
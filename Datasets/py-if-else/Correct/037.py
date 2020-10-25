#!/bin/python3a
a= int(input())

if(a%2==1):
       print("Weird")  
elif(a%2==0 and a>=2 and a<=5):
    print("Not Weird")
elif(a%2==0 and a>=6 and a<=20):
    print("Weird")
elif(a%2==0 and a>20):
    print("Not Weird")
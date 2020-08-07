#!/bin/python3
number = int(input())
if ((number%2 != 0) or ((number%2 == 0) and (6 <= number <= 20))):
	print ('Weird')
elif ((number%2 == 0) and ((2 <= number <= 5) or (number > 20))) :
	print ('Not Weird')

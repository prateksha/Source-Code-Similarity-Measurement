def ensure(x,y):  #used to ensure that in function gcd, a is greater than b, since this is required for the euclidian algorithm, which divides a by b in the first step.
	return x>y

def gcd(a,b):
	a=abs(a)  #used to ensure that the function works even if a and b are negative. Note that gcd(a,b) = gcd(|a|,|b|).
	b=abs(b)
	if(ensure(a,b)):
		if(a!=0 and b==0): # if one of the numbers is 0, then the other number becomes the gcd.
			return a
		elif(a%b==0): #If a is divisible by b, then b is the gcd.
			return b
		else:
			return gcd(b,a%b) #Euclid's algorithm repeatedly divides the divisor of the previous division with the remainder of the previous division, until the remainder becomes 0.
	else:
		if(a==0 and b==0):
			return None  #gcd of 0 and 0 is undefined.
		return gcd(b,a)

num1=int(input('enter number one:'))
num2=int(input('enter number two:'))
print ('gcd of',num1,'and',num2,'is',gcd(num1,num2))
	

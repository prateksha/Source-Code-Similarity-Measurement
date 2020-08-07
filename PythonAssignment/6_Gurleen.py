x=int(input("enter a number:"))
y=int(input("enter another one:"))
def ensure(x,y):
	if(x>y):
		return True

def gcd(x,y):
	if(ensure(x,y)):

		if(y==0):
			return x		
		return gcd(y,x%y)
print ("the gcd is:", gcd(x,y))


#This chceks if x is greater than y or not.

def ensure(x,y):
	if x>y:
		return True

#Computes the greatest common divisor.
def gcd(x,y):
    if ensure(x,y)==True:
        if (x!=0 and y==0):
            return x 
        elif(x%y==0):
            return y
        else:
            return gcd(y,x%y)
			
    elif (x==y):
        if(x==0 and y==0):
            return None
        else:
            return x
    else:
        print ("Please enter the numbers in correct order.")

a=int(input("Enter x "))
b=int(input("Enter y "))
print (gcd(a,b))

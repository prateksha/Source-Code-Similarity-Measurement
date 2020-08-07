def ensure(x,y):
    if (x>y):
        return True
    else:
        return False
x = int(input ("input the first number :"))
y = int(input ("input the second number : "))
#the following conversion to positive numbers is to calculate gcd of negative numbers.
if (x < 0):
    x = -1*x
if (y < 0):
    y = -1*y

def gcd(x,y):
    quo = x/y
    rem = x - quo*y
    if (rem == 0):
        return x/quo
    return gcd(y,rem)

if(ensure(x,y) == True):
   print (gcd(x,y))
else:
    print (gcd(y,x))

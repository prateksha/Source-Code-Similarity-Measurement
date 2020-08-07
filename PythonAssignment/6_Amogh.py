def ensure(x,y):
    if x >= y:
        return True
    else:
        return False
a = int(input("Enter the other number:"))
b = int(input("Enter the number:"))
if ensure(a,b) == True:
    k = b
else:
    k = a
def gcd(x,y):
    if ensure(x,y) == True:
        if x == y:
            return y
        elif (x % y == 0) & (k % y == 0):
            return y
        else:
            return gcd(x,y-1)          
    else:
       return gcd(y,x)      
print(gcd(a,b))
def ensure(x, y):
  if(x > y):
    return True
  else:
    return False
def gcd(x, y):
  if(ensure(x, y)):
    if(x % y == 0):
      return y
    else:
      return gcd(y, x%y)
  else:
    return gcd(y, x)
print (gcd(int(input("Enter number 1: ")), int(input("Enter number 2: "))))

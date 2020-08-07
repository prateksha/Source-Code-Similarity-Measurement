def ensure(a,b):
  return a>b
def gcd(a,b):
 if ensure(a,b):
   if a%b == 0:
     return b
   else:
     return gcd(b,a%b)
 else:
  return gcd(b,a)
if __name__ == "__main__":
    a = int(input("Enter a number:"))
    b = int(input("Enter a number:"))
    print (gcd(a,b))

def ensure(x,y):
    return x>y

def gcd(x,y):
    if ensure(x,y):
        temp = x % y
        if temp == 0:
            return y
        else:
            return gcd(y,temp)
    else:
        return gcd(y,x)
if __name__ == "__main__":
    print (gcd(int(input("Enter first number: ")),int(input("Enter second number: "))))
x = int(input ("Enter the first number: "))
y = int(input ("Enter the second number: "))

# This is recursive function achieves exactly what Euclid's algorithm for GCD does.
def gcd(x,y):
    if (x < 0):
        x = abs(x)
    if (y < 0):
        y = abs(y)

    # This helper function checks if x is greater than y.
    def ensure(x,y):
        if (x>y):
            return True
        else:
            return False

    if (ensure(x,y) and y != 0):
        r = x%y # This gives the remainder when x is divided by y.
        return gcd(y,r) # Recursion starts here.
    elif (ensure(x,y) == False and x != 0):
        r = y%x # This gives the remainder when y is divided by x.
        return gcd(x,r) # Recursion starts here.
    # Any number divides 0 evenly. The following lines take care of that.
    if (x == 0):
        return y
    if (y == 0):
        return x


print ("The gcd of the numbers you gave as input is:", gcd(x,y))

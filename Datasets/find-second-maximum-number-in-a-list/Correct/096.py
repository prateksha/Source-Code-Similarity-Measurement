N = input().strip()
X = input().strip().split()

def maxlst(a):
    k=-101
    for j in X:
        if int(j) >= int(k):
            k=j 
    return k

y=maxlst(X)
while y in X:
    X.remove(y)
    
if len(X) == 1:
    print (X[0])
else:
    z=maxlst(X)
    print(z)
    
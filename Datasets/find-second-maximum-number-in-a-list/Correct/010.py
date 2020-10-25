input()
A = list(map(int, input().split()))
prev=-1000
cur=A[0]
for i in range(0,len(A)):
    if(A[i]>cur):
        cur=A[i]
for i in range(0,len(A)):
    if(A[i]>prev and A[i]<cur):
        prev=A[i]
print (prev)
st=input()
s=k=0
l=len(st)
for i in range(l):
    if st[i] in ('A','E','I','O','U'):
        k+=l-i
    else:
        s+=l-i
        
if s>k:
    print("Stuart",s)
elif k>s:
    print("Kevin",k)
else:
    print("Draw")
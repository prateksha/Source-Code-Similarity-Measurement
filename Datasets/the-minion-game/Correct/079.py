d=input()
v=['A','E','I','O','U']
d=list(d)
sf=0
ki=0
kf=t1=t2=0
for i in range(0,len(d)):
    s=k=0
    if d[i] in v:
        k+=1
        t1=len(d)-(i+1)
        ki=t1+k
        kf+=ki
    else:
        s+=1
        t2=len(d)-(i+1)
        si=t2+s
        sf+=si
if sf>kf:
    print('Stuart',sf)
elif kf>sf:
    print('Kevin',kf)
else:
    print('Draw')
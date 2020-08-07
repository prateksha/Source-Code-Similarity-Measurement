S=input()
V=['A','E','I','O','U']
cK,cS=0,0
l=len(S)

for i in range(len(S)):
    if S[i] in V:
#        cK+=len(S[i:])
        cK+=l-i
    else:
#        cS+=len(S[i:])
        cS+=l-i

if cK>cS:print('Kevin',cK)
elif cK<cS:print('Stuart',cS)
else:print('Draw')

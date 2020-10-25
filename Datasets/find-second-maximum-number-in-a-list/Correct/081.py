N=int(input())
lis=[]
for x in input().split():
    val=int(x);
    if lis.count(val)==0:
       lis.append(val)
    
lis.sort()
print(lis[len(lis)-2])
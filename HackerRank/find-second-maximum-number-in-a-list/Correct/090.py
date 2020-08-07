n=int(input())
a=[]
a = [int(x) for x in input().split()]
    
k=set(a)
d=list(k)
d.sort(reverse=True)
print (d[1])


        
    
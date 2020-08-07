N = int(input())
lst = list(map(int,input().split()))
firstlargest = max(lst)
a = list()
for i in range(len(lst)):
    if(lst[i]!=firstlargest):
        a.append(lst[i])
secondlargest = max(a) 
print(secondlargest)
    

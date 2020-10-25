n = int(input())
a = list(map(int,input().strip().split()))
a.sort()
m = max(a)
while max(a) == m:
    a.remove(m)
    
print(a[len(a)-1])
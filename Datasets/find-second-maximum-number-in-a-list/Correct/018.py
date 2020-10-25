input()
l = list(map(int,input().split()))

a = max(l)
while a in l:
    l.remove(a)
print(max(l))
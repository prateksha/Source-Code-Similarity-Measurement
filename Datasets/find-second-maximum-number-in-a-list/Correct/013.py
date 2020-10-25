i=int(input())
lis=list(map(int, input().strip().split(" ")))[:i]
y=max(lis)
while max(lis)==y:
    lis.remove(y)
print(max(lis))
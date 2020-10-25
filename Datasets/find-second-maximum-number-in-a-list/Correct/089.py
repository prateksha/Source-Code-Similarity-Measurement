N = int(input())
A = list(map(int,input().split()))
A.sort()
biggest = A.pop()
i = biggest
while i == biggest:
    i = A.pop()
print(i)
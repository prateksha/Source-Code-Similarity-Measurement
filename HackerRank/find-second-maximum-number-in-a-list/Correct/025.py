n = int(input())
A = list(set(map(int, input().split())))
A.sort()
print(A[len(A)-2])
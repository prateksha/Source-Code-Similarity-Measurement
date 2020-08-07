from heapq import nlargest

N = int(input())
A = {int(a) for a in input().split()}
result = nlargest(2, A)[1]
print(result)
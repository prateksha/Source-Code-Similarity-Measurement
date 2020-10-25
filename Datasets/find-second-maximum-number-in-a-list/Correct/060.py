N = int(input())

lis = list(map(int, input().split()))[:N]
z = max(lis)
while max(lis) == z:
	lis.remove(max(lis))

print(max(lis))

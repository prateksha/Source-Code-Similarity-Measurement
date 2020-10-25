input()
n = set(map(int, input().split()))
print(sorted(n, reverse=True)[1])
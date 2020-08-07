N = int(input())
myset = set(int(i) for i in input().strip().split())
print(sorted(myset)[-2])
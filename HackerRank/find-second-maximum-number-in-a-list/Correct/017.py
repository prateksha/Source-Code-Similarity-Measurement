N = int(input())
lyst = [int(x) for x in input().split(' ')]
print(sorted(set(lyst))[-2])

a = int(input())
s = set([int(x) for x in input().split(" ")])
l = sorted(list(s))

print(l[-2])
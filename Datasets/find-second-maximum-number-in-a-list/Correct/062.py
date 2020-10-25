input()
s=list(set([int(i) for i in input().split(' ')]))
s.sort()
print(s[-2])
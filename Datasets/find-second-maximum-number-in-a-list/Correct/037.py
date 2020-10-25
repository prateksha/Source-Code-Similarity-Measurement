n = input().strip()
a = set(map(int, [x for x in input().strip().split(' ')]))
print(sorted(list(a))[-2])
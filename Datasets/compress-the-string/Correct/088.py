from itertools import groupby
s = input()
S = groupby(s)
print(*[(len(list(y)), (int(x))) for x, y in S])
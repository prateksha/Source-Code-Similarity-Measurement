from itertools import groupby
s = input()
print(*[(len(list(c)), int(k)) for k, c in groupby(s)])
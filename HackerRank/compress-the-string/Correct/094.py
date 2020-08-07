from itertools import groupby
a = input()
print(*[(len(list(g)), int(k)) for k, g in groupby(a)])
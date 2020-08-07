from itertools import groupby

s = input()

print(*[(len(list(g)), int(k)) for k,g in groupby(s)])
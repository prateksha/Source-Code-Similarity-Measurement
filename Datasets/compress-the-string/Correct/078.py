from itertools import groupby

S = input()

print(*[(len(list(g)), int(k)) for k, g in groupby(S)], sep=" ")
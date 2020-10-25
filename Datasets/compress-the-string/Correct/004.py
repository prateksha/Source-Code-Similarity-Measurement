from itertools import groupby
s = input().strip()
res = [(len(list(g)),int(k)) for k,g in groupby(s)]
print(" ".join(map(str, res)))
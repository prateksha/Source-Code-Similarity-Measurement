from itertools import groupby

seq = input().strip()
for x, y in groupby(seq):
    print((len(list(y)), int(x)), end=" ")
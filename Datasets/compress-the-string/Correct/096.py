from itertools import groupby

print(" ".join([str((len(list(g)), int(k))) for k, g in groupby(input().strip())]))
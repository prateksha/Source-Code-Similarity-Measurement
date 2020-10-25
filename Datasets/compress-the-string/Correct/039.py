from itertools import groupby

S = input()

print(" ".join([str((len(list(g)), int(k))) for k, g in groupby(S)]))
 

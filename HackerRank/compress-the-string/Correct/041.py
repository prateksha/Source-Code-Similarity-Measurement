from itertools import groupby

s = input()

tuples = []
for k, g in groupby(s):
    occs = len(list(g))
    tuples.append((occs, int(k)))

print(' '.join([str(t) for t in tuples]))


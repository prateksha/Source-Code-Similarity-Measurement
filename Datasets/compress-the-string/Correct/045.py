from itertools import groupby
stri = list(map(int, input()))

groups = []
uniquekeys = []
for k, g in groupby(stri):
    groups.append(list(g))
    uniquekeys.append(k)

l = [(len(i), j) for i, j in zip(groups, uniquekeys)]
for i in l:
    print(i, end=" ")
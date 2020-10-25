from itertools import groupby
data=input()
for k, g in groupby(data):
    print((len(list(g)),int(k)),end=" ")
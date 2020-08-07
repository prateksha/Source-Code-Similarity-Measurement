chars = input()
from itertools import groupby
lst = [list(g) for k, g in groupby(chars)]

for i in lst:
    print(tuple((len(i),int(i[0]))), end = ' ')
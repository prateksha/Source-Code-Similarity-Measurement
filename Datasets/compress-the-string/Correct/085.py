s=input().strip()
from itertools import groupby
res =[]
for k, g in groupby(s):
    res.append('({}, {})'.format(len(list(g)), k))
print(' '.join(res))
    
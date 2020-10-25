from itertools import groupby

s = input().strip()
a = []

for key, count in groupby(s):
    a.append('({}, {})'.format(len(list(count)), key))

print(' '.join(a))
from itertools import groupby
S = input().strip()

groups = []
for key, group in groupby(S):
    groups.append((len(list(group)), int(key)))

print(*groups, sep=' ')
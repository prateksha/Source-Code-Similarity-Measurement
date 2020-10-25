import itertools
S = input()
groups=[]
for k,g in itertools.groupby(S):
    groups.append((len(list(g)),int(k)))
print(" ".join([str(g) for g in groups]))
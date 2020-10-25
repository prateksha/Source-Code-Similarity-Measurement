import itertools
for i, j in itertools.groupby(input()):
    print(tuple((len(list(j)), int(i))), end = ' ')
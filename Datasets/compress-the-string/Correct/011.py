import itertools
data = input()

groups = []
uniquekeys = []
for k, g in itertools.groupby(data):
    groups.append(list(g))      # Store group iterator as a list
    uniquekeys.append(k)

for g, k in zip(groups, uniquekeys):
    print("({0}, {1})".format(len(g), k), end=" ")
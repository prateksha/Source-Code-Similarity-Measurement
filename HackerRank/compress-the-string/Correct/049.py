import itertools
s = input()

for key, group in itertools.groupby(s):
    print((len(list(group)), int(key)), end=" ")
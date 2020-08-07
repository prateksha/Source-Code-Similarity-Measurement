from itertools import groupby

sample = input()
for key, group in groupby(sample):
    print ((len(list(group)), int(key)), end=' ')

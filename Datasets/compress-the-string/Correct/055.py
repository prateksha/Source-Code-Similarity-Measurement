import itertools
s = list(input())
print(" ".join(map(lambda a: str((len(list(a[1])), int(a[0]))), itertools.groupby(s))))
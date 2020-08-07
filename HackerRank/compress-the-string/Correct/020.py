import itertools

print(" ".join(["(%d, %s)"%(len(list(g)), k) for k, g in itertools.groupby(input())]))
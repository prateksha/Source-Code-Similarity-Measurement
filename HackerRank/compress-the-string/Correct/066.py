import itertools as it

s = input()

print(' '.join([ str( (len(list(v)), int(k)) ) for (k, v) in it.groupby(s) ]))

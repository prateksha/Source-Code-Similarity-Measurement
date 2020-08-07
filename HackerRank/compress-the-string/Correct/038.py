import itertools
s = input() 
print(*[(len(list(b)), int(a)) for a,b in itertools.groupby(s)])
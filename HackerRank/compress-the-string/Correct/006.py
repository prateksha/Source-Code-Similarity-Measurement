   
from itertools import groupby

S = input()
for c, X in groupby(S):
    print(tuple((len(list(X)), int(c))),end=' ')
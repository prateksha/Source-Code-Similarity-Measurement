from itertools import groupby

chars=input()
##chars=sorted(input())

for key,group in groupby(chars):
    print(tuple((len(list(group)),int(key))), end=' ')
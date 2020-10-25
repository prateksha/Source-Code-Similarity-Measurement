from itertools import groupby
s = input()
myList = []
for k,g in groupby(s):
    myList.append((len(list(g)),int(k)) )

print(*myList)



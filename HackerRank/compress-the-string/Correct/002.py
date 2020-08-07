from itertools import groupby
s = input()
print (*[(len(list(group)),int(key)) for key, group in groupby(s)])
    
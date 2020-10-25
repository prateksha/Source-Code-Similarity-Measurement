from itertools import groupby

data = str(input()).strip()
print(*[(int((len(list(j)))),int(i)) for i,j in groupby(data)])

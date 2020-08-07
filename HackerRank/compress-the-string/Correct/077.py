from itertools import groupby

line = input()

for i, j in groupby(line):
    result = (len(list(j)), int(i))
    print(result, end=' ')
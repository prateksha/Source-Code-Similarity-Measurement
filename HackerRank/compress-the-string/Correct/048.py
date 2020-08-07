from itertools import groupby

print (' '.join([ str((len(list(y)), int(x))) for x, y in groupby(input().strip()) ]))

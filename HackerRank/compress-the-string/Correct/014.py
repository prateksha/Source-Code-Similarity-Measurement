from itertools import groupby

print(' '.join([ '({}, {})'.format(len(list(c)), i) for i, c in groupby(input()) ]))
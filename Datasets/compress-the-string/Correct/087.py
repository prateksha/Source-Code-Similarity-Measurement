from itertools import groupby
ls = input()
for k, g in groupby(ls, lambda x: x):
    print('({0}, {1})'.format(len([a for a in g]), k), end =' ')

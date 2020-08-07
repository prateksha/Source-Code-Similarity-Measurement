from itertools import *

s = input()
num = [int(k) for k, g in groupby(s)]
num_occ = [len(list(g)) for k, g in groupby(s)]

for i in zip(num_occ, num):
    print(i, end=' ')
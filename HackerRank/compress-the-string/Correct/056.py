from itertools import *

k = input()

ll = [list(g) for k,g in groupby(k)]

for i in ll:
    qq = (len(i), (int(i[0])))
    print(qq, end=' ')



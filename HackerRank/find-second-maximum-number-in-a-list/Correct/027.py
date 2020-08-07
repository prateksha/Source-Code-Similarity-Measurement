#!/bin/python3

import sys


m = int(input().strip())
marr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
mlist = list(marr)

mlist.sort(reverse=True)

for item in mlist:
    if item != mlist[0]:
        print(item)
        break


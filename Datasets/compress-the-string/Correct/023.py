#https://www.hackerrank.com/challenges/compress-the-string
from itertools import groupby
print(*[(len(list(c)), int(k)) for k, c in groupby(input())]) #RunLengthCoding
from itertools import groupby

nums = [int(i) for i in input()]

print(*[(sum(map(lambda x: 1, g)), k) for k, g in groupby(nums)])
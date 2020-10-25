from itertools import groupby

data = list(int(item) for item in input())

for k, g in groupby(data):
	t = 0
	for n in g:
		t+= 1
	print(tuple([t, k]), end=" ")
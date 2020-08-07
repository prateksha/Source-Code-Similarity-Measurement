from itertools import groupby

my_list = map(int, input())

groups = groupby(my_list)

print(" ".join(list("({0}, {1})".format(len(list(v)), k) for k, v in groups)))

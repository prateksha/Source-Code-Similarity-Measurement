input()
_list = [int(x) for x in input().split()]

first_max = None
second_max = None
for i in _list:
    if first_max is None:
        first_max = i
        continue

    if i > first_max:
        second_max = first_max
        first_max = i
        continue

    if i == first_max:
        continue

    if second_max is None:
        second_max = i
        continue

    if i > second_max:
        second_max = i

print(second_max)
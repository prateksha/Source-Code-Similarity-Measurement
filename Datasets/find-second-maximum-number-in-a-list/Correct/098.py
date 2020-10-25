from collections import OrderedDict

n = input()
a = input()
l1 = a.split()
l2 = list(map(int,l1))
l2.sort(reverse = True)
l3 = list(OrderedDict.fromkeys(l2))
print(l3[1])
n = input()
a = input()
ls = list(map(int, a.split()))
maximum = max(ls)
count = ls.count(maximum)
for i in range (0,count):
    ls.remove(maximum)
print(max(ls))

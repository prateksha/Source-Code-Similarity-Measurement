lst = input() == 0 or list(map(int, input().split()))
n = max(lst)
'''
for i in lst:
    if i == n:
        lst.remove(i)
'''
while max(lst) == n:
    lst.remove(n)
print(max(lst))
import sys
input()
a = list(map(int, input().split()))
m2 = m1 = -sys.maxsize
for i in a:
    if i > m1:
        if i > m2:
            m1, m2 = m2, i
        elif i < m2:
            m1 = i
print(m1)

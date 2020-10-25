n = int(input())
l = list(map(int, input().split(' ')))
l2 = list(l)
m1 = -1000
while len(l) > 0:
    new = l.pop()
    if new > m1:
        m1 = new
m2 = -1000
while len(l2) > 0:
    new = l2.pop()
    if new > m2 and new != m1:
        m2 = new
print(m2)
            
            
def addlists(l1,l2):
  l = list(zip(l1,l2))
  return list(map(sum,l))

def maxlists(l1,l2):
  l = list(zip(l1,l2))
  return list(map(max,l))

def processlists(f,l1,l2):
  return f(l1,l2)

l1=[1,2,3,4]
l2=[4,3,2,8]

print(maxlists(l1,l2))
print(addlists(l1,l2))
print(processlists(addlists,l1,l2))

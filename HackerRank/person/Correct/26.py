def add_lists(l1,l2):
  return [x + y for x,y in zip(l1,l2)]
def maxlist(l1,l2):
  return list(map(max,list(zip(l1,l2))))
def process_lists(f,l1,l2):
   return f(l1,l2)
l1 = eval(input("Enter a list:"))
l2 = eval(input("Enter another list with same length:"))

print(add_lists(l1,l2))
print(maxlist(l1,l2))
print(process_lists(add_lists,l1,l2))
print(process_lists(maxlist,l1,l2))

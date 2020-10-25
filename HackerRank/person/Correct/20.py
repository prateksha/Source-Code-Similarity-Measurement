def processlists(f,l1,l2):
    m = list(map(f,list(zip(l1,l2))))
    return m
l1 = [int(x) for x in input().split()]
l2 = [int(x) for x in input().split()]
def addlists(l1,l2):
    return [i[0]+i[1] for i in zip(l1,l2)]
def maxlists(l1,l2):
    return [max(i[0],i[1]) for i in zip(l1,l2)]
sum1 = lambda i:i[0]+i[1]
max1 = lambda i:max(i[0],i[1])
#This uses the above 2 functions and plugs them in the above higher order function processlists
print(processlists(sum1,l1,l2))
print(processlists(max1,l1,l2))

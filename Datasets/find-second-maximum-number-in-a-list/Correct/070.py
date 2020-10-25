#get input lenght
N = int(input().strip())

#get input
a = [int(x) for x in input().strip().split(' ')]

#get max
maxVal = max(a)

#get second max
secondMaxVal = max([x for x in a if(x < maxVal)])

#print
print(secondMaxVal)
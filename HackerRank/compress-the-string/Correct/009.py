from itertools import groupby
sample=input()

for x,y in groupby(sample,lambda x: x[0]):

    print ("(%d, %s)"%(len(list(y)),x), end=" ")
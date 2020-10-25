from itertools import groupby

chars = input().rstrip()

groups=[]

for k, v in groupby(chars):
    groups.append((len(list(v)), int(k)))
    
print(" ".join(['(%s, %s)' %(k, v) for k, v in groups]))    
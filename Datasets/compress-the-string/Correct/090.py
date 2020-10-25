from itertools import groupby
string = [int(l) for l in list(input())]
tups = [(len(list(k)),i) for i,k in groupby(string)]
print(*tups,sep=' ')
             

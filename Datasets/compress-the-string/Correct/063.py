from itertools import groupby;
s = input().strip();

for key,group in groupby(s,key=None):
    print("("+str(len(list(group)))+", "+str(key)+") ",end="",sep=" ");
N = int(input())
tmp = list(input().split())
nlist = list(map(int,tmp))
del(tmp)
nlist.sort()
for i in range(N-1,0,-1):
    if nlist[i]>nlist[i-1]:
        print(nlist[i-1])
        break
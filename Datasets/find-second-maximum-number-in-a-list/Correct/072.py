n=int(input())

ls=input().split(' ')
ls=[int(ls[i]) for i in range(0,n)]

print(sorted(list(set(ls)),reverse=True)[1])
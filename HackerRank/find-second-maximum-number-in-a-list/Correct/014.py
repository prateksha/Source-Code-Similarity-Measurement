_,x = input(),[int(i) for i in input().split()]
print(max([i for i in x if i != max(x)])) 
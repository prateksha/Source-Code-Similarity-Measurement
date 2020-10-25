n = int(input())
inp = input()
lis = [int(i) for i in inp.split()]
s = set(lis)
lis = list(s)
lis.sort()
    
print(lis[-2])
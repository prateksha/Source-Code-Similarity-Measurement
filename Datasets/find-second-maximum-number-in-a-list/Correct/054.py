n = input()

mylist = input()

mylist = list(map(int,mylist.split()))

mylist = sorted(list(set(mylist)))

print(mylist[-2])
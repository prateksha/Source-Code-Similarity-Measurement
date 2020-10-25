n = input()
nlist = input().split()
nlist = list(map(int, nlist))
largest = nlist[0]
secLargest = None
for i in range(len(nlist)):
    if nlist[i] > largest:
        temp = largest
        largest = nlist[i]
        secLargest = temp
    elif nlist[i] < largest:
        if secLargest == None:
            secLargest = nlist[i]
        elif nlist[i] > secLargest:
            secLargest = nlist[i]
    
print(secLargest)
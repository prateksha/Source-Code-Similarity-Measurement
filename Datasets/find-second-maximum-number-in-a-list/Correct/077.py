numOfItems = input()
listNum = list(map(int,input().split()))
#print(listNum)
for i in range(1):
    #find the max item
    maxItem = max(listNum)
    #print(maxItem)
    
    #remove all duplicates
    while max(listNum) == maxItem:
        listNum.remove(maxItem)
    #print(listNum)
    
#print out new max (2nd max)
print(max(listNum))
    
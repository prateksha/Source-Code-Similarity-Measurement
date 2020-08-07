a = int(input())

if( a <=10 and a>=2):
    temp = input()
   
lis = temp.split()
newlist = list(map(int,lis))
newlist.sort()
max = newlist[len(newlist)-1]
if(max <=100 and newlist[0]>=-100):
    max2=max
    i = len(newlist)-1
    while(max2 == max):
        i=i-1
        max2= newlist[i] 
print(max2)        
        
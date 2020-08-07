n=int(input())
if not(2<= n and n<=10):
    while not(2<= n and n<=10):
        n=int(input())
        
li=input().strip().split(" ")
lis=list(map(int,li))
list=list(set(lis))
#print(list)
wrong=False
#for e in list:
i=0
while not(wrong) and i < len(list):
    if not(-100<=list[i] and list[i]<=100):
        wrong=True
        print("{0} is not between -100 and 100".format(list[i]))
    i+=1

if not(wrong):
    list.sort()
    print(list[-2])
n=input().strip().split()


test=False
values=[s for s in n[0] if s.isdigit() and 0<=int(s)<=9]

if (len(values)>0):
 test=True

target=[]

def adds(samplee):
    global target
    target.append(samplee)
i=0


if 1<=len(n[0])<=10**4 and test:
 while i < len(n[0]):
  count=1
  if i==len(n[0])-1 and n[0][i]!=n[0][i-1]:
   temp = []
   temp.append(count)
   temp.append(int(n[0][i]))
   sample = tuple(temp)


  while i<len(n[0])-1 and n[0][i]==n[0][i+1]:
    count+=1
    i+=1

  temp=[]
  temp.append(count)
  temp.append(int(n[0][i]))
  sample=tuple(temp)




  i+=1
  adds(sample[:])


 for l in target:
    print (l,end='')
    print (" ",end='')

else:
    pass
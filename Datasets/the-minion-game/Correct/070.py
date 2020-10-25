string=input()
count1=0
count2=0
for i in range(0,len(string)):
    if string[i] in('aeiouAEIOU'):
        count1+=len(string)-i
    else:
        count2+=len(string)-i
if count1>count2:
    print('Kevin'+' '+str(count1))
elif count2>count1:
    print('Stuart'+' '+str(count2))
else:
    print('Draw')

S = input()

count = 1
last = "a"

for i in S:
    if int(i) == last:
        count += 1
    else:
        if last == 'a':
            last = int(i)
            count = 1
        else:
            print(tuple([count, last]), end = ' ')
            last = int(i)
            count = 1
        
        
print(tuple([count, last]))
S = input()
stuart = int(0) 
kevin = int(0)
length = len(S)
for i in range(0, length):
        if S[i:i+1] in "AEIOU":
            kevin += (length - i)
        else:
            stuart += (length - i)
   # for j in range(i+1, len(S) +1):
   #     if S[i:i+1] in "AEIOU":
   #         kevin +=1
   #     else:
   #         stuart +=1
    
if stuart > kevin:
    print('Stuart {}'.format(stuart))
elif kevin > stuart:
    print('Kevin {}'.format(kevin))
else:
    print('Draw')
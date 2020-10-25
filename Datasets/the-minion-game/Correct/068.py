S=input()
N=len(S)
vowels='AEIOU'
Stuart_score=0
Kevin_score=0
pos=0
for letter in S:
    if letter in vowels:
        Kevin_score+=N-pos
    else:
        Stuart_score+=N-pos
    pos+=1

if Stuart_score>Kevin_score:
    print('Stuart',Stuart_score)
#    print('Kevin',Kevin_score)
elif Kevin_score>Stuart_score:
#    print('Stuart',Stuart_score)
    print('Kevin',Kevin_score)
else:
    print('Draw')

S = input()
score_S = 0
score_K = 0
for i in range(len(S)):
        if S[i] in "AEIOU":
            score_K += (len(S)-i) 
        else :
            score_S += (len(S)-i) 
            
if score_K>score_S:
    print('Kevin',score_K,sep=' ')
    
elif score_S>score_K:
    
    print('Stuart',score_S,sep=' ')
else:
    print('Draw')


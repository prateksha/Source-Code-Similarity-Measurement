
consonants = ('B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'X', 'Z', 'W', 'Y')
vowels = ('A', 'E', 'I', 'O', 'U')

stuart_score = 0

kevin_score = 0

S = input()
slen = len(S)
for i in range(0, slen):
    if S[i] in consonants:
        stuart_score += slen - i
    else:
        kevin_score += slen - i

if kevin_score == stuart_score:
    print('Draw')
    exit()
if stuart_score > kevin_score:
    print('Stuart', stuart_score)
else:
    print('Kevin', kevin_score)
S = input()
def minion(string):
    Kevin = 0 #Vowel
    Stuart = 0 #Constant
    n = len(S)
    for start in range(n):
        if S[start] in('A', 'E', 'I', 'O', 'U'):
            Kevin += n - start
        else:
            Stuart += n - start
        #for end in range(start, n):
        #    if string[start:end + 1][0] in "AEIOU":
        #        Kevin += 1
        #    else:
        #        Stuart += 1
    #for word in words_in_str:
    #    if word[0] in "AEIOU":
    #        Kevin += 1
    #    elif word[0] not in "AEIOU":
    #        Stuart += 1
    if Stuart > Kevin:
        print("Stuart", Stuart)    
    elif Kevin > Stuart:
        print("Kevin", Kevin)
    else:
        print("Draw")
minion(S)
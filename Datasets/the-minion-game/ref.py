def isVowel(s):
    return s=='A' or s=='I' or s=='U' or s=='E' or s=='O'

def minion_game(s):
    pS = 0
    pK = 0
    for i in range(0, len(s)):
        if(isVowel(s[i])):
            pK = pK + len(s) - i
        else:
            pS = pS + len(s) - i
    if(pS > pK):
        print("Stuart", pS)
    elif(pS < pK):
        print("Kevin", pK)
    else:
        print("Draw")
s = input()
#words = {}
stuart_score, kevin_score = 0,0
for i in range(0,len(s)):
    is_vowel = s[i] in "AEIOU"
    #for j in range(0,len(s)-i):
        #word = s[i:len(s)-j]        
    if (is_vowel):
        kevin_score += len(s)-i
    else:
        stuart_score += len(s)-i
if (kevin_score > stuart_score):
    print ("Kevin " + str(kevin_score))
elif (stuart_score > kevin_score):    
    print ("Stuart " + str(stuart_score))
else:
    print("Draw")    
        
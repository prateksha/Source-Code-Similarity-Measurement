vowel = 'AEIOU'
string = input()
stuartlist = 0
kevinlist = 0

def getList(word,index, wordlist):
    start = index
    for i in range(start, len(word)):
        print(wordlist)
        wordlist +=1

for i in range(len(string)):
    if string[i].upper() in vowel:
        kevinlist = kevinlist + len(string)-i
    else:
        stuartlist = stuartlist + len(string)-i
if stuartlist > kevinlist:
    print("Stuart",stuartlist)
elif stuartlist == kevinlist:
    print("Draw")
else:
    print("Kevin",kevinlist)   
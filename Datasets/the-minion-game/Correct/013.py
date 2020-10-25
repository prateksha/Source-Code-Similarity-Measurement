word = input()

vowels = ['A', 'E', 'I', 'O', 'U']
cscore = 0
vscore = 0

for i in range(len(word)):
    if word[i] in vowels:
        vscore += (len(word)-i)
    else:
        cscore += (len(word) -i)

if vscore > cscore:
    print("%s %s" % ("Kevin", vscore))
elif vscore < cscore:
    print("%s %s" % ("Stuart", cscore))
else:
    print("Draw")
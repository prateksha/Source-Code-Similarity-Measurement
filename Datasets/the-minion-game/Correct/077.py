def minion_game(string):
    vowels = 0
    cons = 0
    for i in range(len(string)):
        if string[i] in 'AEIOU':
            vowels += len(string)-i
        else:
            cons += len(string)-i

    #print("Vovels: " + str(vowels))
    #print("Cons: " + str(cons))

    if(vowels>cons):
        print("Kevin " + str(vowels))
    elif(vowels == cons):
        print("Draw")
    else:
        print("Stuart " + str(cons))
import operator

VOWELS = "AEIOU"

def points(word):
    kevin_words  = 0 # vowels
    stuart_words = 0 # consonants
    for i in range(len(word)):
        if word[i] in VOWELS:
            kevin_words += len(word) - i
        else:
            stuart_words += len(word) - i
    return stuart_words, kevin_words

def minion_game(string):
    stuart, kevin = points(string)
    if stuart == kevin:
        print('Draw')
    elif stuart > kevin:
        print('Stuart ' + str(stuart))
    else:
        print('Kevin ' + str(kevin))


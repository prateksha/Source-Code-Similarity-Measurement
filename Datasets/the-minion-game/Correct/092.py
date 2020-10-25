def minion_game(string):
    string = string.upper()
    vowels = ['A', 'E', 'I', 'O', 'U']
    kevin_score, stuart_score = 0, 0
    for i in range(0, len(string)):
        if string[i] in vowels:
            kevin_score = kevin_score + len(string) - i
        else:
            stuart_score = stuart_score + len(string) - i

    if stuart_score > kevin_score:
        print('Stuart {}'.format(stuart_score))
    elif stuart_score < kevin_score:
        print('Kevin {}'.format(kevin_score))
    else:
        print('Draw')
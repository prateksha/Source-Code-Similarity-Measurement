def minion_game(string):
    # your code goes here
    l = len(string)
    vowels = ['A', 'E', 'I', 'O', 'U']
    stuart, kevin = [0, 0]
    for i in range(l):
        if string[i] in vowels:
            kevin += (l - i)
        else:
            stuart += (l - i)
    if stuart > kevin:
        print('Stuart ' + str(stuart))
    elif stuart == kevin:
        print('Draw')
    else:
        print('Kevin ' + str(kevin))
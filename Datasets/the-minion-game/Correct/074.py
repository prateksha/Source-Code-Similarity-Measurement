def minion_game(string):
    vowels = ['A', 'E', 'I', 'O', 'U']
    
    kevin = 0
    stuart = 0
    n = len(string)

    for i in range(len(string)):
        if string[i] in vowels:
            kevin += n - i
        else:
            stuart += n - i
    
    if kevin == stuart:
        print('Draw')
    elif kevin > stuart:
        print('Kevin', kevin)
    else:
        print('Stuart', stuart)
        
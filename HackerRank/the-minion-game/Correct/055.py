def minion_game(string):
    vowels =['A', 'E', 'I', 'O', 'U']
    length = len(string)
    stuart = 0
    kevin = 0
    for i in range(len(string)):
        diff = length - i
        if string[i] in vowels:
            kevin += diff
        else:
            stuart += diff
    if stuart > kevin:
        result = 'Stuart {}'.format(stuart)
    elif kevin > stuart:
        result = 'Kevin {}'.format(kevin)
    else:
        result = 'Draw'
    print(result)
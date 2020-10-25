def minion_game(s):
    stuart = 0
    kevin = 0

    for i, c in enumerate(reversed(s), start=1):
        if c in 'AEIOU':
            kevin += i
        else:
            stuart += i

    if stuart > kevin:
        print('Stuart', stuart)
    elif kevin > stuart:
        print('Kevin', kevin)
    else:
        print('Draw')

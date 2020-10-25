def minion_game(string):
    stuart = 0
    kevin = 0
    for index,char in enumerate(string.lower()):
        if char in ['a','e','i','o','u']:
            kevin += len(string) - index
        else:
            stuart += len(string) - index
    if stuart > kevin:
        print('Stuart', stuart)
    elif kevin > stuart:
        print('Kevin', kevin)
    else:
        print('Draw')
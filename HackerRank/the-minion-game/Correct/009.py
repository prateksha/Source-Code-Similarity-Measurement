def minion_game(string):
    v = "AEIOU"
    stuart, kevin = 0, 0
    ln = len(string)

    for i in range(ln):  
        if string[i] in v:
            kevin += ln - i
        else:
            stuart += ln - i
        
    if stuart > kevin:
        print('Stuart', stuart)
    elif stuart == kevin:
        print('Draw')
    else:
        print('Kevin', kevin)
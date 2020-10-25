def minion_game(string):
    c1=0
    c2=0
    for i in range(len(string)):
        if string[i:i+1] in 'aeiouAEIOU':
            c1=c1+len(string)-i
        else:
            c2=c2+len(string)-i
    if c1>c2:
        print('Kevin',c1)
    if c2>c1:
        print('Stuart',c2)
    if c1==c2:
        print('Draw')
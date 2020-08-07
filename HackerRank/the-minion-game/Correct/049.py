def minion_game(string):
    vowel='AEIOU'
    S=K=0
    n=len(string)
    for i, v in enumerate(string):
        if v in vowel:
            K+=n-i
        else:
            S+=n-i
    if K>S:
        print('Kevin %d' %K)
    elif K<S:
        print('Stuart %d' %S)
    else:
        print('Draw')
    # your code goes here
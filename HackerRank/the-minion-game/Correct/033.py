def minion_game(string):
    vowels = ['A','E','I','O','U']
    stuartscore = 0
    kevinscore = 0
    
    for i in range(len(string)):
        if string[i] in vowels:
            kevinscore += len(string)-i
        else:
            stuartscore += len(string)-i

    
    if stuartscore > kevinscore:
        print('Stuart', stuartscore)
    elif kevinscore > stuartscore:
        print('Kevin', kevinscore)
    else:
        print('Draw')
        
    
    # your code goes here
from string import ascii_uppercase as up
Vow = list('AEIOU')
Con = [elem for elem in list(up) if elem not in Vow] 
def minion_game(string):
    k, n = 0, 0
    l = len(string)
    for i in range(l):
        if string[i] in Con:
            k += l-i
        elif string[i] in Vow:
            n += l-i
    if k > n:
        print('Stuart', k)
    elif k < n:
        print('Kevin', n)
    else:
        print('Draw')
            
        

    # your code goes here
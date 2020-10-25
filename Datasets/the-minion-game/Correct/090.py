def minion_game(s):
    s = s.upper()
    # your code goes here
    r = [0,0]
    for i,c in enumerate(s):
        r[c in 'AEIOU'] += len(s) - i
    if r[0] > r[1]:
        print("Stuart", r[0])
    elif r[1] > r[0]:
        print("Kevin", r[1])
    else:
        print("Draw")
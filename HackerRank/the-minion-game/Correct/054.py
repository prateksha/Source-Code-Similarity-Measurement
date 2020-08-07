def minion_game(string):
    vowels = ["A","E","I","O","U"]
    Stuart, Kevin = 0,0
    size = len(string)
    for n,i in enumerate(string):
        score = size - n
        if i in vowels:
            Kevin = Kevin + score
        else:
            Stuart = Stuart + score
   
    if (Kevin > Stuart):
        print("Kevin", Kevin)
    elif (Kevin < Stuart):
        print("Stuart", Stuart)
    else:
        print("Draw")
             
def minion_game(s):
    l=len(s)
    s=list(s)
    stuart=0
    kevin=0
    for ii in range(l):
        if s[ii]=="A" or s[ii]=="O" or s[ii]=="U" or s[ii]=="I" or s[ii]=="E":
            kevin=kevin+(l-ii)
        else:
            stuart=stuart+(l-ii)
                
    if kevin>stuart:
        print("Kevin",kevin)
    elif kevin<stuart:
        print("Stuart",stuart)
    elif kevin==stuart:
        print("Draw")
              
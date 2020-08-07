def minion_game(string):
    # your code goes here
    vowels = "AEIOU"
    stuart = 0
    kevin = 0
    for start in range(0,len(string)):
        if string[start] in vowels:
            kevin+=len(string)-start
        else:
            stuart+=len(string)-start



    
    if kevin>stuart:
        print ("Kevin",kevin)
    elif stuart>kevin:
        print ("Stuart",stuart)
    else:
        print ("Draw")

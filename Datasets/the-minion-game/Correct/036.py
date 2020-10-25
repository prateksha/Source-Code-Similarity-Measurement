def minion_game(string):
    lenstr = len(string)
    num1=0
    num2=0
    index = 0
    for a in string:
        if (a.lower()=='a' or a.lower()=='e' or a.lower()=='i' or a.lower()=='o' or a.lower()=='u'):
            num1 += lenstr-index
        else:
            num2 += lenstr-index
        index += 1
    if num1 > num2: 
        print("Kevin",num1)
    elif num1 < num2:
        print("Stuart",num2)
    else:
        print("Draw")
    
    # your code goes here
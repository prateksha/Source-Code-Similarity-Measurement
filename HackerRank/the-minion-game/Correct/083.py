def Kevin(string):
    if string[0] in ['a','e','i','o','u']:
        return True
    else: return False
    

def minion_game(string):
    # your code goes here
    stuart=0
    kevin=0
    string=string.lower()
    
    #create all possible substrings
    for i in range(0,len(string)):
        hehe=len(string)-i
        if Kevin(string[i]):
            
            kevin+=hehe
        else:
            stuart+=hehe
            
    #3k=sum(kevin.values())
    if stuart>kevin:
        print('Stuart '+str(stuart))
    elif kevin>stuart:
        print('Kevin '+str(kevin))
    else:
        print('Draw')
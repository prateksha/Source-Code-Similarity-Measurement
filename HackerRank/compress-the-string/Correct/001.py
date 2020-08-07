s = input()

if (len(s) == 1):
    print ('(1, ' + s + ')')
else :
    ind = 0 
    cnt = 1
    while (ind < len(s) - 1):
        if (s[ind] == s[ind+1]):
            cnt += 1 
        else : 
            print ('(' + str(cnt) + ', ' + s[ind] + ')' , end = ' ')
            cnt = 1 
        
        ind += 1 
    
    print ('(' + str(cnt) + ', ' + s[len(s)-1] + ')' , end = ' ')
        
        
    
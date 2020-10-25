def minion_game(string):
    # your code goes here
       vowels = 'AEIOU'

       kevin, stuart = 0, 0

       for i in range( len(string) ):
              if string[i] in vowels:
                     kevin += len(string) - i
              else:
                     stuart += len(string) - i

       if kevin > stuart:
              print( "Kevin " + str(kevin) )
       elif stuart > kevin:
              print("Stuart " + str(stuart) )
       else:
              print("Draw")
        
            
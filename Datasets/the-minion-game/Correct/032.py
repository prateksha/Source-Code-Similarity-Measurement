# Enter your code here. Read input from STDIN. Print output to STDOUT

S = input()

stuart, kevin = (0,0)

vowels = list('AEIOU')

for x in range(len(S)):
    if S[x] in vowels:
        kevin += len(S) - x
    else:
        stuart += len(S) - x
        
if kevin < stuart:
    print("Stuart " + str(stuart))
elif stuart < kevin:
    print("Kevin " + str(kevin))
else:
    print("Draw")
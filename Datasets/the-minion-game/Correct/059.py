'''
https://www.hackerrank.com/challenges/the-minion-game
This problem is interesting by looking at the problem differently.

'''
s = input()

vowels = 'AEIOU'

kevsc = 0
stusc = 0
for i in range(len(s)):
    if s[i] in vowels:
        kevsc += (len(s)-i)
        #print('kevsc is',kevsc)
    else:
        stusc += (len(s)-i)
        #print('stusc is',stusc)

if kevsc > stusc:
    print("Kevin", kevsc)
elif kevsc < stusc:
    print("Stuart", stusc)
else:
    print("Draw")
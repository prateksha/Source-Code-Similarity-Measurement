s = input()

vowels = set('AEIOU')

stuart = 0
kevin = 0 # vowels

for i, letter in enumerate(s):
    score = len(s) - i
    if letter in vowels:
        kevin += score
    else:
        stuart += score
        
if stuart > kevin:
    print('Stuart', stuart)
elif kevin > stuart:
    print('Kevin', kevin)
else:
    print('Draw')
        
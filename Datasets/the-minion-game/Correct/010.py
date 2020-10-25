s = input()
vowels = set('AEIOU')
KevinScore = StuartScore = 0
for i in range(len(s)):
    if s[i] in vowels:
        KevinScore += len(s)-i
    else:
        StuartScore += len(s)-i
if KevinScore == StuartScore:
    print("Draw")
else:
    print('Kevin {}'.format(KevinScore) if KevinScore > StuartScore else 'Stuart {}'.format(StuartScore))
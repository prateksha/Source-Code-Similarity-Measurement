from sys import stderr


s = input().strip().upper()

vowels = 'AEIOU'

score = {'Stuart':0, 'Kevin':0}

for x in range(len(s)):
    if s[x] in vowels:
        score['Kevin'] += len(s) - x
    else:
        score['Stuart'] += len(s) - x

print(score, file=stderr)

if score['Kevin'] != score['Stuart']:
    winner = max(score,key=score.get)
    print(winner,score[winner])
else:
    print('Draw')

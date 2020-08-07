#!/usr/bin/env python3

S = input()
length = len(S)
scores = {'Stuart': 0, 'Kevin': 0}
for index, letter in enumerate(S):
  if letter in ['A', 'E', 'I', 'O', 'U']:
    scores['Kevin'] += length - index
  else:
    scores['Stuart'] += length - index
if scores['Kevin'] == scores['Stuart']:
  print('Draw')
else:
  print(max(scores, key=scores.get), max(scores.values()))

### v0.1 too slow
#import itertools
#
#S = input()
#combi_range = itertools.combinations(range(len(S)+1), 2)
#scores = {'Stuart': 0, 'Kevin': 0}
#for combi in combi_range:
#  if S[combi[0]:combi[1]][0] in ['A', 'E', 'I', 'O', 'U']:
#    scores['Kevin'] += 1
#  else:
#    scores['Stuart'] += 1
#if scores['Kevin'] == scores['Stuart']:
#  print('Draw')
#else:
#  print(max(scores, key=scores.get), max(scores.values()))

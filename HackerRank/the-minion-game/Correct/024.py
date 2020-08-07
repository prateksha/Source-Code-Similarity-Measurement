word = input()

def score(w, fn):
  sz = len(w)
  s = 0
  for i in range(sz):
    if fn(w[i]):
      s += sz - i
  return s
    
stuart = score(word, lambda x: x not in "AEIOU")
kevin = score(word, lambda x: x in "AEIOU")

if stuart == kevin:
  print("Draw")
elif stuart > kevin:
  print("Stuart {}".format(stuart))
else:
  print("Kevin {}".format(kevin))
    
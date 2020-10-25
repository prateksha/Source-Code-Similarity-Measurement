import itertools

s = input()

l = [] 
for k, g in itertools.groupby(s):
	t = (k, len(list(g)))
	l.append(t)

s = ""
for t in l:
	s += "(" + str(t[1]) + ", " + t[0] + ") " 

print(s.rstrip())

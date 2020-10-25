n = input()
l = len(n)
v,c = 0,0
for i in range(0,len(n)):
	if n[i] in ['A','E','I','O','U']:
		t = l-i
		v += t
	else:
		t = l-i
		c += t
if c>v:
	print ('Stuart',c)
elif v>c:
	print ('Kevin',v)
else:
	print ('Draw')
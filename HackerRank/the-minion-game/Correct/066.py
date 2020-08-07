s = input()
n = len(s)
lc, lv = 0, 0
for i in range(0,n):
    if s[i] in 'AEIOU': lv += n-i
    else: lc += n-i
if lc > lv : print('Stuart', lc)
elif lc == lv: print('Draw')
else: print('Kevin', lv)
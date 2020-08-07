s = input()
leng = len(s)
st = 0
kv = 0
for i in range(leng):
    if s[i] in ['A', 'E', 'I', 'O', 'U']:
        kv = kv + leng-i
    else:
        st = st + leng-i
        
if st > kv:
    print("Stuart %d"%st)
elif kv > st:
    print("Kevin %d"%kv)
else:
    print("Draw")
            
            
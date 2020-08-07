s = input()
kev = 0
stu = 0
for i in range(len(s)):
    j = str.find("AEIOU",s[i])
    if j >= 0:
        kev += len(s) - i
    else:
        stu += len(s) - i

if kev > stu:
    print("Kevin {0}".format(kev))
elif stu > kev:
    print("Stuart {0}".format(stu))
else:
    print("Draw")

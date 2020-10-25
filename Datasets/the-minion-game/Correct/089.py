
vowels = set("AEIOU")

str = input()

kevin = 0
stuart = 0

for i in range(len(str)):
    if str[i] in vowels:
        kevin += len(str) - i
    else:
        stuart += len(str) - i
        
if kevin == stuart:
    print("Draw")
elif kevin > stuart:
    print("Kevin {0}".format(kevin))
else:
    print("Stuart {0}".format(stuart))

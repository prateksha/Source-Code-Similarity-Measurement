string = input()
stuart = 0
kevin = 0
for i in range(len(string)):
    if string[i] in ["A", "E", "I", "O", "U"]:
        kevin += len(string) - i
    else:
        stuart += len(string) - i
if kevin > stuart:
    print("Kevin", kevin)
elif kevin < stuart:
    print("Stuart", stuart)
else:
    print("Draw")
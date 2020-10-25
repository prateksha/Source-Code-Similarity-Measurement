def minion_game(string):
    string.upper()
    vowels = "AEIOU"
    Stu, Kev = 0, 0
    Stu = sum([len(string) - i for i in range(len(string)) if string[i] not in vowels])
    Kev = sum([len(string) - i for i in range(len(string)) if string[i] in vowels])
    if Stu > Kev:
        print("Stuart", Stu)
    elif Stu < Kev:
        print("Kevin", Kev)
    else:
        print("Draw")
    
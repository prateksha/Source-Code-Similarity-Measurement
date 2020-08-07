def minion_game(string):
    vowels = ['A', 'E', 'I', 'O', 'U']
    n = len(string)
    Kevin = 0
    for i in range(n):
        if string[i] in vowels:
            Kevin += n - i
    n *= n + 1
    n /= 2
    n = int(n)
    Stuart = n - Kevin
    if Stuart == Kevin:
        print("Draw")
    elif Stuart > Kevin:
        print("Stuart {0}".format(Stuart))
    else:
        print("Kevin {0}".format(Kevin))
        
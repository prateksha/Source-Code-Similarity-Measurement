def get_all_substrings(input_string):
    length = len(input_string)
    if (length < 0):
        return [input_string]
    return [input_string[i:j+1] for i in range(length) for j in range(i,length)]

def minion_game(string):
    # your code goes here
    score_stuart = 0
    score_kevin = 0
    
    vovels = ['A', 'E', 'I', 'O', 'U']
    # substrings = get_all_substrings(string)
    for x in range(len(string)):#substrings:
        if string[x] in vovels:#x[0] in vovels:
            score_kevin += len(string) - x
        else:
            score_stuart += len(string) - x
    if score_kevin > score_stuart:
        print('Kevin', score_kevin)
    elif score_kevin < score_stuart:
        print('Stuart', score_stuart)
    else:
        print('Draw')
def count_substrings(input_string, starts_with_vowel):
    substring_counter = 0
    string_length = len(input_string)
    
    for i in range(string_length):
        if not starts_with_vowel ^ (input_string[i] in 'AEIOU'):
            substring_counter += (string_length - i)
            
    return substring_counter

def minion_game(string):
    stuart_score = count_substrings(string, starts_with_vowel=False)
    kevin_score = count_substrings(string, starts_with_vowel=True)
    
    if (stuart_score > kevin_score):
        print('Stuart ' + str(stuart_score))
    elif (stuart_score < kevin_score):
        print('Kevin ' + str(kevin_score))
    else:
        print('Draw')
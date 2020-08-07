def is_vowel(letter):
    return letter in ['a', 'e', 'i', 'o', 'u', 'y']

def score_words(words):
    score = 0
    for word in words:
        contv = 0
        for w in word:
            if is_vowel(w):
                contv += 1
        if contv % 2 == 0:
            score += 2
        else:
            score += 1
    return score            
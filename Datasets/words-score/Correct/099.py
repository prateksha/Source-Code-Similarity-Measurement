def is_vowel(letter):
    return letter in ['a', 'e', 'i', 'o', 'u', 'y']

def score_words(words):
    score = 0
    for word in words:
        count = 0
        for letter in word:
            if is_vowel(letter):
                count += 1
        score += 1
        if count%2 == 0:
            score += 1
    return score
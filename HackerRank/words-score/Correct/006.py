def is_vowel(letter):
    return letter in ('a', 'e', 'i', 'o', 'u', 'y')

def score_words(words):
    scores = [sum(1 if is_vowel(letter) else 0 for letter in word) for word in words]    
    return sum(1 if (score & 1) else 2 for score in scores)
def is_vowel(letter):
    return letter in ['a', 'e', 'i', 'o', 'u', 'y']

def score_words(words):
    ans = [2 if len(list(filter(lambda x:is_vowel(x),list(word))))%2==0 else 1 if len(list(filter(lambda x:is_vowel(x),list(word))))%2==1 else 0 for word in words]
    return sum(ans)

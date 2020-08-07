def score_words(words):
    score = 0
    for w in words:
        t=0
        for i in "aeiouy":
            t+=w.count(i)
        if(t%2!=0):
            score+=1
        else:
            score+=2
        
    return score
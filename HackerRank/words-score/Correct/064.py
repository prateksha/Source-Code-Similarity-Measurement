def score_words(words):
    l=list()
    count=0
    su=0
    letter=['a','e','i','o','u','y']
    for i in words:
        for j in i:
            for t in letter:
                if t==j:
                    count=count+1
        if count%2==0:
            s=2
            l.append(s)
        else:
            s=1
            l.append(s)
        count=0
    for u in l:
        su=u+su
    return su
import itertools

s = list(input())

res = [(sum(1 for i in g), int(k)) for k, g in itertools.groupby(s)]

print(*res)
    


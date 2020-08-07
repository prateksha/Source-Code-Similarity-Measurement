input()
lista = list(set(map(int, input().split())))
print(sorted(lista,reverse=True)[1])

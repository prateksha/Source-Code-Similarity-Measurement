x = input()
a = input()

print(sorted(set(map(int, a.split(' '))), reverse=True)[1])

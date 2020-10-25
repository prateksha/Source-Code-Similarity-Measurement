iter= int(input())
lt2=(str(input())).split()
lt=[int(i) for i in lt2]
lt.sort()
lt.reverse()
c=lt.count(lt[0])
for i in range(c):
    lt.remove(lt[0])
print(lt[0])

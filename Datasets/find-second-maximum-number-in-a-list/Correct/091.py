n = int(input())
n_list = input().split()
i = 0
for x in n_list:
    n_list[i] = int(x)
    i += 1

n_list.sort()
n_list.reverse()

prev = n_list[0]

for i in n_list:
    cur = i
    if cur == prev:
        prev = i
        continue
    else:
        print (cur)
        break
    
n = int(input())
arr = sorted(list(map(int, input().split(' '))), reverse=True)

p = arr[0]
for x in arr:
    if x != p:
        print(x)
        break
    p = x
    
    
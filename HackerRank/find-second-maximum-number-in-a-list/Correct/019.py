N = int(input())
array = list(map(int, input().split()))

max_array = max(array)

bill = -101
for a in array:
    if a < max_array and a > bill:
        bill = a

print(bill)
        
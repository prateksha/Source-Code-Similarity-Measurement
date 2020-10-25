n = int(input())
l = (int(x) for x in input().split(' '))

largest = -101
second_largest = -101
for num in l:
    if num > largest:
        second_largest, largest = largest, num
    elif num > second_largest and num != largest:
        second_largest = num

print(second_largest)
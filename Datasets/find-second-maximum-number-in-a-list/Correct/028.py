N, A = int(input()), [int(number) for number in input().split()]
largest_number = -101
second_largest_number = -101

for x in A:
    if x > largest_number:
        second_largest_number = largest_number
        largest_number = x
    elif x < largest_number and x > second_largest_number:
        second_largest_number = x
    
print(second_largest_number)
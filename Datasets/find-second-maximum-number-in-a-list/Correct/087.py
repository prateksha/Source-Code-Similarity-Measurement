n = int(input())

numbers_list = set(map(int, input().split(' ')))

numbers_list = list(numbers_list)
numbers_list.sort()

print(numbers_list[-2])
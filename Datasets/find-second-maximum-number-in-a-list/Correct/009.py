_ = input()
numbers = set([int(val) for val in input().split()])
print(sorted(numbers)[-2])
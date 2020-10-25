n = int(input())
numbers = list(map(int,input().split()))
numbers.sort()
if numbers.count(max(numbers))== 1:
    second = numbers[-2]
else:
    for i in range(numbers.count(max(numbers))):
        numbers.remove(max(numbers))
    second = numbers[-1]
print(second)

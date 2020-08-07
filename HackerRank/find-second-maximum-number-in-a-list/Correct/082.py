input()

l = [int(n) for n in input().split()]

highest = -101
second_highest = -101

for n in l:
	if n > highest:
		second_highest = highest
		highest = n
	elif n >= second_highest and n != highest:
		second_highest = n

print(second_highest)
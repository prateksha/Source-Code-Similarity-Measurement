from sys import stdin
data = stdin.read().strip().split()[1:]

nums = list(map(int, data))
nums.sort(reverse=True)
big = nums[0]

for n in nums[1:]:
	if n != big:
		print(n)
		break


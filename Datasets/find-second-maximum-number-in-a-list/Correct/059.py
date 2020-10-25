

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

arr = [x for x in arr if x!= max(arr)]
print (max(arr))
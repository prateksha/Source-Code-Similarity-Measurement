n = int(input())
arr = list(map(int,input().split()))
max = -100
for i in range(n):
    if arr[i] > max:
        max = arr[i]     
arr = [x for x in arr if x != max] 
max = -100
for i in range(len(arr)):
    if arr[i] > max:
        max = arr[i] 
        
print(max)        
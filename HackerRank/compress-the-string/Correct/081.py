arr = list(input())

result_arr = list()

while arr:
    count = 1
    for j in range(len(arr)-1):
        if len(arr) != 1:
            if arr[j] == arr[j+1]:
                count+=1
                if j == len(arr)-2:
                    result_arr.append((count, int(arr[j]))) 
            else:
                result_arr.append((count, int(arr[j])))
                break

    if len(arr) == 1:
        result_arr.append((count, int(arr[0]))) 

    arr = arr[count:]
            
for item in result_arr:
    print(item, end=" ")
            
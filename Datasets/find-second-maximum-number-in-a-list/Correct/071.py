def remove_values_from_list(the_list, val):
    return [value for value in the_list if value != val]

n = int(input())
question_list = input().split()
question_list = list(map(int, question_list))
question_list.sort()
largest_num = question_list[n-1]
#print(largest_num)
result_list = remove_values_from_list(question_list, largest_num)
print(result_list[-1])
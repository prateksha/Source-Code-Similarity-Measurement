string = input().strip()

stuart_points = 0
kevin_points = 0

str_length = len(string)
for i in range(str_length):
    ch = string[i]

    if ch in ['A', 'E', 'I', 'O', 'U']:
        kevin_points += (str_length - i)
    else:
        stuart_points += (str_length - i)

if stuart_points > kevin_points:
    print('{0} {1}'.format('Stuart', stuart_points))
elif kevin_points > stuart_points:
    print('{0} {1}'.format('Kevin', kevin_points))
else:
    print('Draw')
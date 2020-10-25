
input_str = input()
output_lst = []

count = 0
prev_elem = ''

for elem in input_str :
    
    if prev_elem == '' :
        prev_elem = elem
        count += 1
        
    elif prev_elem != elem : 
        output_lst.append((count,(int)(prev_elem)))
        prev_elem = elem
        count = 1
        
    else :
        count += 1

output_lst.append((count,(int)(prev_elem)))
        
for elem in output_lst :
    print(elem,end=' ')

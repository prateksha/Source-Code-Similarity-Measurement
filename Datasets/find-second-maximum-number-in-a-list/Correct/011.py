num_elements = int(input().strip())
elements = list(set(map(int, (input().split()))))

elements.remove(max(elements))
second_largest = elements.pop(elements.index(max(elements)))
print(second_largest)
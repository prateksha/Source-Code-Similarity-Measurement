length = int(input())
array = input()
array = array.split()
array1 = []
bufer = 0

bufer = int(array.pop())
for i in range(1, length):
	buf_buf = int(array.pop())
	if bufer == buf_buf: continue
	if bufer > buf_buf: array1.append(buf_buf)
	if bufer < buf_buf:
		array1.append(bufer)
		bufer = buf_buf

array1.sort()
print(array1[-1])

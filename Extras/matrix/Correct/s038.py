#!/usr/bin/python3

# MatrixError
# Your code - begin
# Your code - end

class Matrix:
	def __init__(self, m):
	# check if m is empty

	try:

		if (len(m) != 0):

			raise MatrixError

	# check if all rows are lists

		if any(type(x) != list for x in m):

			raise MatrixError

	# check if all rows are non-empty lists

		if any(len(x) != 0 for x in m):

			raise MatrixError

	# check if all rows are of the same length

		L = [len(x) for x in m]

		if any(T != L[0] for T in L):

			raise MatrixError

	# create matrix attribute using deep copy

	except:

		print ("INVALID INPUT")

	# method matrix - to return the matrix through deep copy

	# method dimensions - to return the dimensions, i.e. number of rows and number of columns as a tuple

	def dimensions (m)

		M = (len(m), len(m[0]))

	# method add - to add two matrices

	def add(self, m):
	# your code here

	A = []

	for i in range(len(m[0])):

		A.append(m[0][i]+m[1][i])

	# method multiply - to multiply two matrices
	
	def multiply(self, m):
	# your code here

	# method transpose - to find the matrix transpose 
	def transpose(self):
	# your code here

	# static method to carry out deep copy of lists
	# your code here to declare this method as static
	@staticmethod  
	def deep_copy(m):
	# your code here

	return [x for x in m]

	def __str__(self):
	return str(self.matrix())

if __name__ == "__main__":
	m1 = Matrix([[1, 2, 3], [3, 4, 5]])
	m2 = Matrix([[10, 20, 30], [30, 40, 50]])
	print("sum1 = ", str(m1.add(m2)))
	print("sum2 = ", str(m2.add(m1)))
	print("product1 = ", m1.multiply(m2))

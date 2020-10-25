#!/usr/bin/python3

# MatrixError
# Your code - begin
# Your code - end

class Matrix:
	def __init__(self, m):
		self.m=m
    # check if m is empty
		if len(m)==0:
			raise MatrixError
    # check if all rows are lists
		for i in self.m :
			if type(i)!=list:
				raise MatrixError
    # check if all rows are non-empty lists
		for i in self.m :
			if len(i)==0:
				raise MatrixError
    # check if all rows are of the same length
		for i in self.m :
			for j in self.m:
				if len(i)!=len(j):
					raise MatrixError    
    # create matrix attribute using deep copy

  # method matrix - to return the matrix through deep copy

  # method dimensions - to return the dimensions, i.e. number of rows and number of columns as a tuple

  # method add - to add two matrices
	def add(self, m):
    # your code here
		sum1=[]
		for i in range(len(m)):
			for j in range(len(m[i])):
				sum1[i][j]=self.m[i][j]+m[i][j]
		return list(sum1)
  # method multiply - to multiply two matrices
	def multiply(self, m):
    # your code here
 		multiply=[]
		for i in range(len(m)):
			for j in range(len(m[i])):
				multiply[i][j] += (self.m[i][j])*(m[j][i])
  # method transpose - to find the matrix transpose 
	def transpose(self):
    # your code here
    
  # static method to carry out deep copy of lists
  # your code here to declare this method as static
	def deep_copy(m):
    # your code here

	def __str__(self):
		return str(self.matrix())

if __name__ == "__main__":
  m1 = Matrix([[1, 2, 3], [3, 4, 5]])
  m2 = Matrix([[10, 20, 30], [30, 40, 50]])
  print("sum1 = ", str(m1.add(m2)))
  print("sum2 = ", str(m2.add(m1)))
  print("product1 = ", m1.multiply(m2))

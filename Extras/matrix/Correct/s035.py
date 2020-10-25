#!/usr/bin/python3

# MatrixError
# Your code - begin
Exception MatrixError
# Your code - end

class Matrix:
	def __init__(self, m):
		k=[]
    # check if m is empty
		if len((m)==0):
			return MatrixError
    # check if all rows are lists
		for i in m:
			if(type(i)!=list):
				return MatrixError
    # check if all rows are non-empty lists
		for i in m:
			if(len(i)==0):
				return MatrixError
    # check if all rows are of the same length
		for i in m:
			if(len(m[0])!=len(i)):
				return MatrixError
    # create matrix attribute using deep copy
		for i in m :
			k.deepcopy(i)
  # method matrix - to return the matrix through deep copy
	def matrix(self):
		return k
  # method dimensions - to return the dimensions, i.e. number of rows and number of columns as a tuple
	def dimensions(self):
		return (len(m),len(m[0]))
  # method add - to add two matrices
	def add(self, m):
    # your code here
		for i in len(m):
			for j in len(m[0]):
				l[i][j]=self.m[i][j]+m[i][j]
		return l
  # method multiply - to multiply two matrices
	def multiply(self, m):
		if((self.m).dimentions[1]!=m.dimensions[0]):
			return MatrixError
		
    # your code here
 
  # method transpose - to find the matrix transpose 
	def transpose(self):
    # your code here
		for i in len(m):
			for j in len(m[0]):
				self.m[i][j]=self.m[j][i]
		return self.m
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

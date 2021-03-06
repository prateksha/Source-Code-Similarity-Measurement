#!/usr/bin/python3

# MatrixError
# Your code - begin
# Your code - end

class Matrix:
  def __init__(self, m):
    self.matrix=m
    # check if m is empty
    if(m==None):
      raise Exception("Matrix Error")
    
    # check if all rows are lists
    for i in m:
      if(type(i)!=list):
        raise Exception("Matrix Error")

    # check if all rows are non-empty lists
    for i in m:
      if(i==None):
        raise Exception("Matrix Error")
    # check if all rows are of the same length
    length=len(m[0])
    for i in m:
      if(len(i)!=length):
        raise Exception("Matrix Error")
    
    # create matrix attribute using deep copy

  # method matrix - to return the matrix through deep copy

  # method dimensions - to return the dimensions, i.e. number of rows and number of columns as a tuple
  def dimensions(self):
    no_rows=len(self.matrix)
    no_columns=len(self.matrix[0])
    return no_rows,no_columns

  # method add - to add two matrices
  #def add(self, m):
    # your code here
       
 
  # method multiply - to multiply two matrices
  #def multiply(self, m):
    # your code here
 
  # method transpose - to find the matrix transpose 
  #def transpose(self):
    # your code here
    
  # static method to carry out deep copy of lists
  # your code here to declare this method as static
  #def deep_copy(m):
    # your code here

  def __str__(self):
    return str(self.matrix())

if __name__ == "__main__":
  m1 = Matrix([[1, 2, 3], [3, 4, 5]])
  m2 = Matrix([[10, 20, 30], [30, 40, 50]])
  #print("sum1 = ", str(m1.add(m2)))
  #print("sum2 = ", str(m2.add(m1)))
  #print("product1 = ", m1.multiply(m2))
  print m1.dimensions()
  print m2.dimensions()

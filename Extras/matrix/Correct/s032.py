#!/usr/bin/python3

# MatrixError
# Your code - begin
# Your code - end

class Matrix:
  def __init__(self, m):
    # check if m is empty
    if not(len(m)!=0):
        raise Exception
    # check if all rows are lists
    if not(for i in m: if m[i] == type(list)):
        raise Exception
    # check if all rows are non-empty lists
    if not(for i in m: if len(m[i]!=0):
        raise Exception
    # check if all rows are of the same length
    if not(for i in range(1, len(m): if len(m[i-1]==len(m[i])):
        raise Exception
    # create matrix attribute using deep copy

  # method matrix - to return the matrix through deep copy

  # method dimensions - to return the dimensions, i.e. number of rows and number of columns as a tuple
  def dimensions(m):
    return (len(m), len(m[1])
  # method add - to add two matrices
  def add(self, m):
    # your code here
    
      
  # method multiply - to multiply two matrices
  def multiply(self, m):
    # your code here
 
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

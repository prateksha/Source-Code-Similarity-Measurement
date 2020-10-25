#!/usr/bin/python3

# MatrixError
# Your code - begin
# Your code - end

class Matrix:
  def __init__(self, m):
    # check if m is empty
    if len(m)==0:
      raise SyntaxError("List cannot be empty.")
    # check if all rows are lists
    for i in m:
      if type(i)!='list':
        raise SyntaxError("Rows must be of type list.")
    # check if all rows are non-empty lists
      elif len(i)==0:
        raise SyntaxError("Rows cannot be empty.")
    # check if all rows are of the same length
    length=len(m[0])
    for i in m:
      if len(i)!=length:
        raise SyntaxError("All rows must be of same length.")
    # create matrix attribute using deep copy
    self.__matrix__=deep_copy(m)
  # method matrix - to return the matrix through deep copy
  def matrix(self):
    return self.__matrix__
  # method dimensions - to return the dimensions, i.e. number of rows and number of columns as a tuple
  def dimensions(self):
    a=len(self.__matrix__)
    b=len(self.__matrix__[0])
    return (a,b)
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

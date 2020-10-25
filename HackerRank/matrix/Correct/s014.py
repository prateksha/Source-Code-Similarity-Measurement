#!/usr/bin/python3

# MatrixError
# Your code - begin
# Your code - end
class MatrixError(Exception):
  def __init__(self):
    Exception.__init__(self)
class Matrix:
  def __init__(self, m):
    # check if m is empty
    if(len(m)==0):
      raise MatrixError()
    # check if all rows are lists
    for i in m:
      if(type(i)!=list):
        raise MatrixError()
    # check if all rows are non-empty lists
    for i in m:
      if(len(i)==0):
        raise MatrixError()
    # check if all rows are of the same length
    x=len(m[0])
    for i in m:
      if(len(i)!=x):
        raise MatrixError
    # create matrix attribute using deep copy
    self.matrix=m[:] 
  # method matrix - to return the matrix through deep copy
  def __matrix__(self):
    return self.matrix
  # method dimensions - to return the dimensions, i.e. number of rows and number of columns as a tuple
  def dimensions(self):
    return (len(self.matrix()),len(self.matrix()[0]))

  # method add - to add two matrices
  def add(self, m):
    l1=[]
    l2=[]
    for i in range(self.matrix()):
      for j in range(self.matrix()[0]):
        l2.append(self.matrix()[i][j]+m.matrix[i][j])
      l1.append(l2)
      l2=[]
    return l1
    
      
  # method multiply - to multiply two matrices
  #def multiply(self, m):
    # your code here
 
  # method transpose - to find the matrix transpose 
 # def transpose(self):
    # your code here
    
  # static method to carry out deep copy of lists
  @static
  def deep_copy(m):
      return self.matrix()[:]

  def __str__(self):
    return str(self.matrix())

if __name__ == "__main__":
  m1 = Matrix([[1, 2, 3], [3, 4, 5]])
  m2 = Matrix([[10, 20, 30], [30, 40, 50]])
  print("sum1 = ", str(m1.add(m2)))
  print("sum2 = ", str(m2.add(m1)))
 # print("product1 = ", m1.multiply(m2))

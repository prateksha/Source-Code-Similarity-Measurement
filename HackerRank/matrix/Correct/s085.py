#!/usr/bin/python3

# MatrixError
# Your code - begin
# Your code - end

class Matrix:
  def __init__(self, m):
    # check if m is empty
    if(len(m)==0):
      raise ValueError('error')
    
    # check if all rows are lists
    for e in m:
      if(not type(e)==list):
        raise ValueError('error')
    
    # check if all rows are non-empty lists
    for e in m:
      if(len(e)==0):
        raise ValueError('error')
    
    # check if all rows are of the same length
    c=len(m[0])
    for e in m:
      if(not len(e)==c):
        raise ValueError('error')
     
    # create matrix attribute using deep copy
    self.__matrix__ = deep_copy(m)   
  # method matrix - to return the matrix through deep copy
  def matrix(self):
      return self.__matrix__

  # method dimensions - to return the dimensions, i.e. number of rows and number of columns as a tuple
  def dimensions(self):
      return (len(self.__matrix__), len((self.__matrix__)[0]))

  # method add - to add two matrices
  def add(self, m):
    # your code here
    l = []
    for i in range(len(m)):
      n=[]
      for j in range(len(m[0])):
        n.append(m[i][j]+(self.__matrix__)[i][j])
      l.append(n[:])
    return l
      
  # method multiply - to multiply two matrices
  def multiply(self, m):
    # your code here
    pass 
  # method transpose - to find the matrix transpose 
  def transpose(self):
    # your code here
    pass
  # static method to carry out deep copy of lists
  # your code here to declare this method as static
  @staticmethod
  def deep_copy(m):
    # your code here
    n=[]
    for e in m:
      if(type(n)==list):
        n.append(deep_copy(m[e]))
      else:
        n.append(e)
    return n
  
  def __str__(self):
    return str(self.matrix())

if __name__ == "__main__":
  m1 = Matrix([[1, 2, 3], [3, 4, 5]])
  m2 = Matrix([[10, 20, 30], [30, 40, 50]])
  print("sum1 = ", str(m1.add(m2)))
  print("sum2 = ", str(m2.add(m1)))
  print("product1 = ", m1.multiply(m2))

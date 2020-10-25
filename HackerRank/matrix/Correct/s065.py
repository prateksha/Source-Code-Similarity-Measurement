#!/usr/bin/python3

# MatrixError
# Your code - begin
# Your code - end

class Matrix:
  def __init__(self, m):
    if(m==[]):
		raise Exception
    for i in m:
      if(i!=list):
        raise Exception

    # check if all rows are non-empty lists
    for i in m:
      if(i==[]):
        raise Exception
    # check if all rows are of the same length
    temp = len(m[0])
    for i in m:
      if(len(i)!=temp):
        raise Exception
      else:
        temp = len(i)
    # create matrix attribute using deep copy
	self.__matrix__ = deep_copy(self,m) 
  # method matrix - to return the matrix through deep copy
  
  # method dimensions - to return the dimensions, i.e. number of rows and number of columns as a tuple
  def dimensions(self):
    k =(len(self.__matrix__),len(self.__matrix__[0]))
    return k 
  # method add - to add two matrices
  def add(self, m):
    z = deep_copy(m)
    for i in range(len(m)-1):
      for j in range(len(m[0]-1)):
        z[i][j] += self.__matrix__[i][j]
    return z   
  # method multiply - to multiply two matrices
  def multiply(self, m):
    # your code here
    for i in range(len(m) - 1):
      for j in range(len(m[0]) - 1):
         
  # method transpose - to find the matrix transpose 
  def transpose(self):
    # your code here
    
  # static method to carry out deep copy of lists
  # your code here to declare this method as static
  @static def deep_copy(self,m):	
    k = []	
      for i in m:
        if(i == list()):
          k.append(deep_copy(i))
        else
          return i
    return k  # your code here

  def __str__(self):
    return str(self.matrix())

if __name__ == "__main__":
  m1 = Matrix([[1, 2, 3], [3, 4, 5]])
  m2 = Matrix([[10, 20, 30], [30, 40, 50]])
  print("sum1 = ", str(m1.add(m2)))
  print("sum2 = ", str(m2.add(m1)))
  print("product1 = ", m1.multiply(m2))

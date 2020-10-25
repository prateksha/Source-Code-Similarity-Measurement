#!/usr/bin/python3

# MatrixError
# Your code - begin

# Your code - end

class Matrix:
  def __init__(self, m):
    
    # check if m is empty
    if (len(m)==0):
      raise Exception
    
    # check if all rows are lists

    for i in m:
      if (type(i)!='list'):
#        raise Exception
        print("Error")
    # check if all rows are non-empty lists

    for i in m:
      if(len(i)==0):
        raise Exception

    # check if all rows are of the same length
    
    length = len(m[0])
    for i in m:
      if(length!=len(i)):
        raise Exception

    # create matrix attribute using deep copy

    self.m = []
    for i in m:
      self.m.append(m[::])


  # method matrix - to return the matrix through deep copy

  def matrix(self):
    return self.m

  # method dimensions - to return the dimensions, i.e. number of rows and number of columns as a tuple

  def dimensions(self):
    self.rows = len(self.m)
    self.columns = len(self.m[0])
    return (self.rows, self.columns)

  # method add - to add two matrices
#  def add(self, m):
    # your code here
#    if (self.dimensions!=m.dimensions):
#      print (self.dimensions, m.dimensions)
     # raise Exception
#    sum = []
#    for i in range(1,len(self.m)+1):
#      for j in range(1,len(self.m[0])+1):
#        sum = self.m[i]+m[i]

#    return sum

  # method multiply - to multiply two matrices
 # def multiply(self, m):
    # your code here
 
  # method transpose - to find the matrix transpose 
#  def transpose(self):
    # your code here
    
  # static method to carry out deep copy of lists
  # your code here to declare this method as static
#  def deep_copy(m):
    # your code here

#  def __str__(self):
#    return str(self.matrix())

if __name__ == "__main__":
  m1 = Matrix([[1, 2, 3], [3, 4, 5]])
  m2 = Matrix([[10, 20, 30], [30, 40, 50]])
  print("sum1 = ", str(m1.add(m2)))
#  print("sum2 = ", str(m2.add(m1)))
#  print("product1 = ", m1.multiply(m2))
  print("dim = ", m1.dimensions())


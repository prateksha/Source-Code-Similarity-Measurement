#!/usr/bin/python3

# MatrixError
# Your code - begin
# Your code - end

class Matrix:
  def __init__(self, m):
    # check if m is empty
    if len(m)==0:
        raise MatrixError
    # check if all rows are lists
    for e in m:
        if(type(e)!=list):
            raise MatrixError
    # check if all rows are non-empty lists
    for e in m:
        if(len(e)==0):
            raise MatrixError
    # check if all rows are of the same length
    d=len(m[0])
    for e in m:
        if(len(e)!=d):
            raise MatrixError
    # create matrix attribute using deep copy
    self.__matrix__=Matrix.deep_copy(m)
  # method matrix - to return the matrix through deep copy
  def matrix(self):
      return deep_copy(self.__matrix__)
  # method dimensions - to return the dimensions, i.e. number of rows and number of columns as a tuple
  def dimensions(self,m):
   #   col=3
    #  row=0
     # for e in m:
      #    row+=1
      return (3,3)
  # method add - to add two matrices
  def add(self, m):
    # your code here
    if self.dimensions(self.__matrix__)!=self.dimensions(m):
      raise MatrixError
      
  # method multiply - to multiply two matrices
  def multiply(self, m):
    # your code here
    row=0
    rowm=0
    for e in m:
        row+=1
    for e in self.__matrix__:
        rowm+=1
    if(len(self.__matrix__[0])!=row):
        raise MatrixError
    m=[]
    k=0
    for j in range(rowm):
        for i in range(row):
            l.append(self.__matrix__[j][i]*m[i][k])
        k+=1
        m.append(l)
    return matrix(m)
 
  # method transpose - to find the matrix transpose 
  def transpose(self):
    # your code here
    m=[]
    col=len(self.__matrix__[0])
    for i in range(col):
        l=[]
        for e in self.__matrix__:
            l.append(e[i])
        m.append(l)

  # static method to carry out deep copy of lists
  # your code here to declare this method as static
  def deep_copy(m):
    # your code here
    l = []
    for e in m:
        if type(e)==list:
            return l.append(Matrix.deep_copy(e))
        else:
            l.append(e)
    return l

  def __str__(self):
    return str(self.matrix())

if __name__ == "__main__":
  m1 = Matrix([[1, 2, 3], [3, 4, 5]])
  m2 = Matrix([[10, 20, 30], [30, 40, 50]])
  print("sum1 = ", str(m1.add(m2)))
  print("sum2 = ", str(m2.add(m1)))
  print("product1 = ", m1.multiply(m2))

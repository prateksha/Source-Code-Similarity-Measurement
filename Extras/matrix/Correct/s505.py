#!/usr/bin/python3

# MatrixError
# Your code - begin
# Your code - end

class Matrix:
  def __init__(self, m):
      self.m=m
      # check if m is empty
      if(len(m)==0):
          return None
      # check if all rows are lists
      # check if all rows are non-empty lists
      if(len(m[0])!=0):
          return None
    # check if all rows are of the same length
    # create matrix attribute using deep copy
  # method matrix - to return the matrix through deep copy

  # method dimensions - to return the dimensions, i.e. number of rows and number of columns as a tuple

  # method add - to add two matrices
  def add(self, m):
      # your code here
      l=[]
      l1=[]
      for i in range(0,len(self.m)):
          for j in range(0,len(self.m[0])):
              l1.append(self.m[i][j]+m[i][j])
          l.append(l1)
      return l    
  # method multiply - to multiply two matrices
  def multiply(self, m):
    # your code here
    l=[]
    l1=[]
    for i in range(0,len(m)):
        for j in range(0,len(m[0])):
            l1.append(self.m[i][j]*m[j][i])
        l.append(l1)
    return l    


  # method transpose - to find the matrix transpose 
  def transpose(self):
    # your code here
    l=[]
    l1=[]
    for i in range(0,len(self.m)):
        for j in range(0,len(self.m[0])):
            l1.append(m[j][i])
        l.append(l1)
    return l    
  # static method to carry out deep copy of lists
  # your code here to declare this method as static
  def deep_copy(m):
    # your code here
    l=[]
    l1=[]
    for i in range(0,len(m)):
        for j in range(0,len(m[0])):
            l1.append(m[i][j])
        l.append(l1)
    return l    


  def __str__(self):
    return str(self.matrix())

if __name__ == "__main__":
  m1 = Matrix([[1, 2, 3], [3, 4, 5]])
  m2 = Matrix([[10, 20, 30], [30, 40, 50]])
  print("sum1 = ", str(m1.add(m2)))
  print("sum2 = ", str(m2.add(m1)))
  print("product1 = ", m1.multiply(m2))

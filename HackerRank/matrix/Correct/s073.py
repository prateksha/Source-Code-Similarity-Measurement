#!/usr/bin/python3

# MatrixError
class MatrixError(Exception):
    def __init__(self,m):
        self.message = m
# Your code - begin
# Your code - end

class Matrix:
  def __init__(self, m):
    # check if m is empty
    if(len(m)==0):
            raise MatrixError("Empty matrix")
    # check if all rows are lists
    for i in m:
        if(type(i) != list):
            raise MatrixError("Not A List")        
    # check if all rows are non-empty lists
    for i in m:
        if(len(i)==0):
            raise MatrixError("Empty List")
    # check if all rows are of the same length
    k = map(len,m)
    a=k[0]
    for i in k:
        if (i != a):
            raise MatrixError("Rows Not Of Same Length")            
    # create matrix attribute using deep copy
    self.matrix = deep_copy(m)
  # method matrix - to return the matrix through deep copy

  # method dimensions - to return the dimensions, i.e. number of rows and number of columns as a tuple
    def dimensions(self):
        return (len(m),len(m[0]))

  # method add - to add two matrices
  #def add(self, m):
    # your code here
      
  # method multiply - to multiply two matrices
  #def multiply(self, m):
    # your code here
 
  # method transpose - to find the matrix transpose 
  #ef transpose(self):
    # your code here
    
  # static method to carry out deep copy of lists
  # your code here to declare this method as static
  def deep_copy(m):
    # your code here
    k=[]
    for i in m:
        if (type(i)==list):
            deep_copy(i)
        else:
            k.append(i)
    return k    

  def __str__(self):
    return str(self.matrix())

if __name__ == "__main__":
  m1 = Matrix([[1, 2, 3], [3, 4, 5]])
  m2 = Matrix([[10, 20, 30], [30, 40, 50]])
  print("sum1 = ", str(m1.add(m2)))
  print("sum2 = ", str(m2.add(m1)))
  print("product1 = ", m1.multiply(m2))

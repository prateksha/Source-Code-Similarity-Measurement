#!/usr/bin/python3

# MatrixError
# Your code - begin
class MatrixError(Exception):
    def __init__(self,err_code):
        if err_code == 1:
            raise Exception("The matrix cannot be empty")
        if err_code == 2:
            raise Exception("All rows should be lists")
        if err_code == 3:
            raise Exception("All rows should be non-empty lists")
        if err_code == 4:
            raise Exception("All rows should be of the same length")
# Your code - end

class Matrix:
  def __init__(self, m):
    # check if m is empty
    if len(m) == 0:
        MatrixError(1)
    # check if all rows are lists
    type_list = [type(x)==list for x in m]
    if False in type_list:
        MatrixError(2)
    # check if all rows are non-empty lists
    len_list = [len(x) for x in m]
    if 0 in len_list:
        MatrixError(3)
    # check if all rows are of the same length
    if len(len_list) != (sum(len_list)/len_list[0]):
        MatrixError(4)
    # create matrix attribute using deep copy
    self.__matrix__ == deep_copy(matrix)
  # method matrix - to return the matrix through deep copy
  @staticmethod
  def deep_copy(l):
    l_copy = []
    for i in l:
        if type(i) != list:
            l_copy.append(i)
        else:
            l_copy.append(deep_copy(i))
    return l_copy
  # method dimensions - to return the dimensions, i.e. number of rows and number of columns as a tuple
  def dimensions(self,m):
    return (len(m),len(m[0])
  # method add - to add two matrices
  def add(self, m):
    # your code here
    sum_matrix = []
    for i in range(len(self.m)):
        sum_matrix.append([])
        for j in range(len(i)):
            sum_matrix[i].append(self.m[i][j]+m[i][j])
    return sum_matrix
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

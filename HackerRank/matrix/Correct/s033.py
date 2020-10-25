#!/usr/bin/python3

# MatrixError
# Your code - begin
# Your code - end

class Matrix:
  def __init__(self, m):
    # check if m is empty
        if m == [] or type(m) != type([]):
            raise MatrixError
    # check if all rows are lists
        for i in m:
            if type(m) != type([]):
                raise MatrixError
    # check if all rows are non-empty lists
            if i == []:
                raise MatrixError
    # check if all rows are of the same length
        
            if len(i) != len(m[0]):
                raise MatrixError
    # create matrix attribute using deep copy
        self.__matrix__ = deep_copy(m)
  # method matrix - to return the matrix through deep copy
  def matrix(self):

     return deep_copy(self.__matrix__)
  # method dimensions - to return the dimensions, i.e. number of rows and number of columns as a tuple
  def dimensions(self):

        return (len(self.__matrix__),len(self.__matrix__[0]))
  # method add - to add two matrices
  def add(self, m):

      summat = []
      rowsum = []

      for i,j in self.__matrix__, m:
        
          rowsum = []

          for k,l in i,j:
              rowsum.append(k+l)

          summat.append(rowsum)


    # your code here
      
  # method multiply - to multiply two matrices
  def multiply(self, m):
    # your code here
 
  # method transpose - to find the matrix transpose 
  def transpose(self):
    # your code here
    i=0
    j=0

    transpose = []

    for i in range(0,len(self.__matrix__[0])):
        temp = []
        for j in range(0,len(self.__matrix__)):
            temp.append(0)

        transpose.append(temp)    

    
    for i in range(0,len(self.__matrix__)):
        for j in range(0,len(self.__matrix__)):
            transpose[j][i]=self.__matrix__[i][j]

  # static method to carry out deep copy of lists
  @staticmethod
  def deep_copy(l):

        copy=[]

        for i in l:

            if type(i) == type([]):
                copy.append(deep_copy(i))
            else:
                copy.append(i)


        return copy

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
 # print("product1 = ", m1.multiply(m2))

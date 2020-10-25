#!/usr/bin/python3

# MatrixError
# Your code - begin
# Your code - end

class Matrix:
    def __init__(self, m):
    # check if m is empty
        if(len(m)==0):
            raise MatrixError
    
    # check if all rows are lists
        for i in m:
            if(type(i) != list):
               raise MatrixError
    
    # check if all rows are non-empty lists
        for i in m:
            if(len(i) == 0):
                raise MatrixError

    # check if all rows are of the same length
        s = len(m[0])
        for i in m:
            if(len(i) != s):
                raise MatrixError
        
    # create matrix attribute using deep copy
        self.__matrix__ = deep_copy(m)

  # method matrix - to return the matrix through deep copy
    @staticmethod
    def deep_copy(l):

        
  # method dimensions - to return the dimensions, i.e. number of rows and number of columns as a tuple
    def dimensions(self):
        row = len(self.__matrix__)
        col =0
        for i in self.__matrix__:
            col += len(i)
        return (row,col)

  # method add - to add two matrices
    def add(self, m):
        # your code here
        if (len(self.__matrix__) != len(m)):
            raise MatrixError
        if (len(self.__matrix__[0]) != len(m[0])):
            raise MatrixError

        for i in range(len(self.__matrix__)):
            for j in range(len(self.__matrix__[i])):
                self.__matrix__[i][j] += m[i][j]
        return self.__matrix__
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

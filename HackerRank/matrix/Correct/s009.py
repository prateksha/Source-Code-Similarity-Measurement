#!/usr/bin/python3

# MatrixError
class MatrixError(Exception):
    def __init__(self,m):
        self.message=m
# Your code - begin
class Matrix:
    def __init__(self,l):
        k=len(l[0])
        if not(len(l)==0):
            for i in l:
                if len(i)!=k or type(i)!='list':
                    raise MatrixError("Error Creating Matrix")
        self.__matrix__=self.deep_copy(l)
    def deep_copy(self,l):
        l=[]
        for i in l:
            l.append([])
            for j in i:
                self.l.append(j)
            return l
    def dimensions(self):
        return (len(self.__matrix__),len(self.__matrix__[0]))
    def add(self,other):
        l=[]
        if self.dimensions()==other.dimensions():
            for i in self.__matrix__:
                l.append([])
                for j,k in self.__matrix__[i],self.__matrix__[i]:
                    l[i].append(j+k)
        else:
            raise MatrixError("Dimensions unequal")
    def multiply(self,other):
        if self.dimensions[1]==other.dimensions[0]:
            
    def transpose(self):
        i=0
        while(i<len(__matrix__)):


                
# Your code - end

class Matrix:
  def __init__(self, m):
    # check if m is empty
    
    # check if all rows are lists

    # check if all rows are non-empty lists

    # check if all rows are of the same length
    
    # create matrix attribute using deep copy

  # method matrix - to return the matrix through deep copy

  # method dimensions - to return the dimensions, i.e. number of rows and number of columns as a tuple

  # method add - to add two matrices
  def add(self, m):
    # your code here
      
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

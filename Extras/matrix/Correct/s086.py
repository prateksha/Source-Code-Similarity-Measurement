#!/usr/bin/python3

# MatrixError
# Your code - begin
# Your code - end

class Matrix:
  def __init__(self, m):
    # check if m is empty
    if m!=[]:
        self.m=m
    # check if all rows are lists
    for i in m:
        if type(i)=list:
            flag=0
        else:
            flag=1
            break
    if (flag==0):
        return m
        

    # check if all rows are non-empty lists
    for i in m:
        if i!=[]:
            flag1=0
        else:
            flag=1
            break
    if (flag1==0):
        return m
   
            

    # check if all rows are of the same length
    list1=[]
    for i in m:
        list1.append(len(i))
    for i in list1:
        for j in list1:
            if i==j:
                flag2=0
            else:
                flag2=1
                break
    if (flag2==0):
        return m

    # create matrix attribute using deep copy

  # method matrix - to return the matrix through deep copy

  # method dimensions - to return the dimensions, i.e. number of rows and number of columns as a tuple

  # method add - to add two matrices
  def add(self, m):
      m=[]
      for i in self.m:
          
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

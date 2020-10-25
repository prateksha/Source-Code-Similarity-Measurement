#!/usr/bin/python3

class MatrixError(Exception):
  def __init__(self, m):
    Exception.__init__(self, m)

class Matrix:
  def __init__(self, m):
    # check if m is empty
    if(len(m) == 0):
      raise(MatrixError("empty matrix"))
    
    # check if all rows are lists
    for row in m:
      if(type(row) != list):
        raise(MatrixError("non-list row"))

    # check if all rows are non-empty lists
    for row in m:
      if(len(row) == 0):
        raise(MatrixError("empty row"))

    # check if all rows are of the same length
    row_len = len(m[0])
    for row in m:
      if(len(row) != row_len):
        raise(MatrixError("unequal rows"))
    
    # create matrix attribute using deep copy
    self.__matrix__ = Matrix.deep_copy(m)

  # to return the matrix through deep copy
  def matrix(self):
    return Matrix.deep_copy(self.__matrix__)

  def dimensions(self):
    num_rows = len(self.__matrix__)
    num_cols = len(self.__matrix__[0])
    return (num_rows, num_cols)

  def add(self, m):
    def add_lists(l1, l2):
      z = zip(l1, l2)
      return [a + b for a, b in z]

    # check if the dimensions are compatible
    if(self.dimensions() != m.dimensions()):
      raise(MatrixError("add failed: incompatible dimensions"))

    array = m.matrix()
    zipped_rows = zip(self.__matrix__, array)
    return Matrix([add_lists(r1, r2) for (r1, r2) in zipped_rows])
      
  def multiply(self, m):
    def sop(l1, l2):
      return sum([a * b for a, b in zip(l1, l2)])

    _, c1 = self.dimensions()
    r2, c2 = m.dimensions()

    # check if the dimensions are compatible
    if(c1 != r2):
      raise(MatrixError("multiply failed: incompatible dimensions " + str(self.dimensions()) + ", " + str(m.dimensions())))

    array = m.matrix()
    newm = []
    for row1 in self.__matrix__:
      newrow = []
      for c in range(c2):
        col2 = [r[c] for r in array]
        newrow.append(sop(row1, col2))
      newm.append(newrow)
    return Matrix(newm)
  
  def transpose(self):
    def get_col(i):
      return [row[i] for row in self.__matrix__]

    _, cols = self.dimensions()
    return Matrix([get_col(i) for i in range(cols)])
    
  # static method to carry out deep copy of lists
  @staticmethod
  def deep_copy(m):
    newm = []
    for e in m:
      if(type(e) == list):
        newm.append(Matrix.deep_copy(e))
      else:
        newm.append(e)
    return newm

  def __str__(self):
    return str(self.__matrix__)

def t1():
  try:
    m = Matrix([])
  except MatrixError as e:
    print(e)

def t2():
  try:
    m = Matrix([[1, 2], 2])
  except MatrixError as e:
    print(e)
  
def t3():
  try:
    m = Matrix([[1, 2], []])
  except MatrixError as e:
    print(e)
  
def t4():
  try:
    m = Matrix([[1, 2], [1]])
  except MatrixError as e:
    print(e)

def t5():
  l = [[1, 2], [3, 4]]
  m = Matrix(l)
  l[1][1] = 40
  print("l = ", l)
  print("m = ", m)
  
def t6():
  l = [[1, 2, 3], [3, 4, 5]]
  m = Matrix(l)
  print("dimensions = ", m.dimensions())

def t7():
  m1 = Matrix([[1, 2, 3], [3, 4, 5]])
  m2 = Matrix([[10, 20, 30], [30, 40, 50]])
  print("sum1 = ", str(m1.add(m2)))
  print("sum2 = ", str(m2.add(m1)))

def t8():
  m1 = Matrix([[1, 2, 3], [4, 5, 6]])
  m2 = Matrix([[7, 10, 13], [8, 11, 14], [9, 12, 15]])
  print("product1 = ", m1.multiply(m2))

def t9():
  try:
    m1 = Matrix([[1, 2], [3, 4]])
    m2 = Matrix([[10, 20, 30], [30, 40, 50]])
    print("sum1 = ", str(m1.add(m2)))
  except MatrixError as e:
    print(e)

def t10():
  try:
    m1 = Matrix([[1, 2, 3], [4, 5, 6]])
    m2 = Matrix([[7, 10, 13], [8, 11, 14]])
    print("product1 = ", m1.multiply(m2))
  except MatrixError as e:
    print(e)

def t11():
  try:
    m2 = Matrix([[7, 10, 13], [8, 11, 14]])
    print("transpose = ", m2.transpose())
  except MatrixError as e:
    print(e)

if __name__ == "__main__":
  t1()
  t2()
  t3()
  t4()
  t5()
  t6()
  t7()
  t8()
  t9()
  t10()
  t11()

#!/usr/bin/python3

import math

# your code for class Shape  -- Q.4(f)
class shape():
    def __init__(self,name):
        self.name=name
# your code for class Triangle -- Q.4(a)
class Triangle():
    def __init__(self,name):
        self.name=name
# code for RegularPolygon is provided below for your use.
class RegularPolygon(shape):
  def __init__(self, n, l, name="Regular Polygon"):
    if(n < 3):
      raise ValueError("Polygons can't have less than 3 sides.")
    Shape.__init__(self, name)
    self.num_of_sides = n
    self.length = l

  def area(self):
    theta = 2 * math.pi / self.num_of_sides
    phi = (self.num_of_sides - 2) * math.pi / (2 * self.num_of_sides)
    b = self.length
    h = (b * math.tan(phi)) / 2
    area_triangle = 0.5 * b * h
    return self.num_of_sides * area_triangle

  def circumference(self):
    return self.num_of_sides * self.length

  def get_side(self):
    return self.length

# your code for class Square -- Q.4(c)
class Square(shape):
    def __init__(self,l,name='Square(5)'):
        shape.__init__(self,name)
        self.length=l
    def area(self):
        return (self.length)*(self.length)
    def circumference(self):
        return 4*(self.length)
# your code for class EquilateralTriangle -- Q.4(c)
class EquilateralTriangle(shape):
    def __init__(self,a,name='EquilateralTriangle(5)'):
        shape.__init__(self,name)
        self.length=a
    def area(self):
        A=((3**0.5)/(4))
        return (A)*(self.length * self.length)
    def circumference(self):
        p=3*(self.length)
        return p

# your code for class Pentagon -- Q.4(d) and Q.4(e)
class Polygon(shape):
    def __init__(self,x,name='Polygon(5)'):
        shape.__init__(self,name)
        self.length=x
    def area(self):
        return (self.length * self.length) + (3**0.5/4)*(self.length * self.length)
    def circumfernce(self):
        return 5*(self.length)

if __name__ == "__main__":
  t1 = EquilateralTriangle(5)
  s1 = Square(5)
  p1 = Polygon(5)
 
  print("t1 = ", t1)
  print("s1 = ", s1)
  print("p1 = ", p1)

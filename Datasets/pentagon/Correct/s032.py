#!/usr/bin/python3

import math

# your code for class Shape  -- Q.4(f)
class Shape:
    def __init__(self, name):
        self.name = name
    def get(self):
        print (str(self.name) + "(area = " + str(RegularPolygon.area()) + ", circumference = " + str(RegularPolygon.circumference()))
# your code for class Triangle -- Q.4(a)
class Triangle(Shape):

    def __init__(self, b, h):
        self.base = b
        self.height = h
    def area(self):
        return 0.5*self.base*self.height

# code for RegularPolygon is provided below for your use.
class RegularPolygon(Shape):
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
class Square(RegularPolygon):

    def __init__(self,l):
        RegularPolygon.__init__(self, 4, l, name="Square")
    def area(self):
        return RegularPolygon.area()
    def circumference(self):
        return RegularPolygon.circumference()

# your code for class EquilateralTriangle -- Q.4(c)
class EquilateralTriangle(RegularPolygon):
    def __init__(self, l):
        RegularPolygon.__init__(self, 3, l, name="EquilateralTriangle")
    def area(self):
        return RegularPolygon.area()
    def circumference(self):
        return RegularPolygon.circumference()

# your code for class Pentagon -- Q.4(d) and Q.4(e)
class Pentagon(RegularPolygon):
    def __init__(self,l):
        EquilateralTriangle.__init__(self,l)
        Square.__init__(self, l)
    def area(self):
        return EquilateralTriangle.area() + Square.area()
    def circumference(self):
        return EquilateralTriangle.circumference() + Square.circumference() - 2*self.length

if __name__ == "__main__":
  t1 = EquilateralTriangle(5)
  s1 = Square(5)
  p1 = Pentagon(5)

  print("t1 = ", t1)
  print("s1 = ", s1)
  print("p1 = ", p1)

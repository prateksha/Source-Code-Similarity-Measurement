#8. (a) Implement a Person with attributes: name , parent , children .
#(b) Implement a class Family (essentially a tree of Person s) with an attribute headOfFamily as
#its root node. Let there be the following methods:
#headOfFamily
#allNodes
#searchNode(n), n being a node.
#allAncestors(n), n being a node.
#parent(n), n being a node.
#depth
#Add more methods and properties if required. Use Person class specifying the parent and
#children of each person. Display the tree at the end.
#(c) Create a family tree familyTree of the following form:
#A-B-(D E F)
#|
#c
#|
#G
#This should get pretty-printed with the following command: print familyTree . The
#printed family tree may appear as follows:
#A
# B
#  D
#  E
#  F
# C
#  G


class Person:
 def __init__(self,n,p,c):
  self.name=n
  self.parent=p
  self.children=c


class Family:
 def __init__(self,hf):
  self.headOffamily=hf
 def headOfFamily(self):
  return self.headOffamily
 def allnodes

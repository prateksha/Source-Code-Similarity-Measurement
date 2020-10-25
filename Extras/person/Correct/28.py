class Person:
 def __init__(self,name,parent,children):
  self.name=name
  self.parent=parent
  self.children=children
class Family:
 familyList=[]
 counter=0
 def __init__(family,person):
  family.familyList.append(person)
  family.headofFamily=family.headOfFamily()
 def headOfFamily(family):
  for i in range(len(family.familyList)):
   if(family.familyList[i].parent==''):
    return family.familyList[i].name
  return None
 def allNodes(family):
  for i in range(len(family.familyList)):
   print(family.familyList[i].name)
  return None
 def allAncestors(family,person):
  i=0
  x=[person.parent]
  y=person
  while(y.parent!=family.headofFamily and y.parent!=''):
   for j in range(len(family.familyList)):
    for k in range(len(family.familyList[j].children)):
     if(y.parent==family.familyList[j].children[k]):
      x.append(family.familyList[j].name)
      y=family.familyList[j] 
  return x
 def depth(family):
  l=[]
  for j in range(len(family.familyList)):
   if(family.familyList[j].children==[]):
    l.append(family.allAncestors(family.familyList[j]))
  l1=[]
  for i in range(len(l)):
   l1.append(len(l[i]))
  return max(l1) 
 def parent(family,person):
  return person.parent
 def searchNode(family,person):
  for i in range(len(family.familyList)):
   if(family.familyList[i]==person):
    return True
 def familyTree(family,Tree):
  family.subTree(Tree[1])
 def subTree(family,Tree):
  family.counter=family.counter+1
  s=''
  for i in range(family.counter):
   s=s+' '
  print(s+Tree[0])
  if(len(Tree)==1):
   family.counter=family.counter-1
  for i in range(1,len(Tree)):
   if(isinstance(Tree[i],list)):
    family.subTree(Tree[i])
   elif(i==len(Tree)-1):
    print(s+Tree[i])
    family.counter=family.counter-1
   else:
    print(s+Tree[i])  
def t1():
 p1=Person('A','',['B','C'])
 p2=Person('B','A',['D','E','F'])
 p3=Person('C','A',['G'])
 p4=Person('D','B',[])
 p5=Person('E','B',[])
 p6=Person('F','B',[])
 p7=Person('G','C',[])
 f1=Family(p2)
 f1=Family(p3)
 f1=Family(p1)
 f1=Family(p4)
 f1=Family(p5)
 f1=Family(p6)
 f1=Family(p7)
 Tree=['A',['B',['D','E','F'],'C',['G']]]
 print(f1.headOfFamily())
 f1.allNodes()
 print(f1.allAncestors(p2))
 print(f1.depth())
 print(f1.searchNode(p5))
 print(f1.parent(p2))
 f1.familyTree(Tree)
if(__name__=="__main__"):
 t1()

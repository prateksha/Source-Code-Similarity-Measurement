class Person:
    def _init_(self,name,parent,children):
        self.name = name
        self.parent = parent
        self.children = children
x = []
class Family:
    def _init_(self,headOfFamily):
        self.rootNode = headOfFamily
    def headOfFamily(self):
        return self.rootNode
    def allNodes(self):
         def f(A):
            subtrees = A
            for x in subtrees.children:
                print(x.name, end=' ')
                if(x.children == []):
                    pass
                else:
                    f(x)
         return f(A)
    @staticmethod    
    def searchNode(n):
          def f(A):
            subtrees = A
            for x in subtrees.children:
                if(n == x.name):
                    print("True")
                else:
                   if(x.children == []):
                       pass
                   else:
                       f(x)
          return f(A)      
    def allAncestors(self,n):
        def f(rootNode):
            global x
            x.append(rootNode)
            for x1 in rootNode.children:
                f(x1)
        f(self.rootNode)
        while(n.parent != ""):
            print(n.parent)
            global x
            for x1 in x:
                if(n.parent == x1.name):
                    n = x1
    def parent(self,n):
        return  n.parent
    @property
    def depth(self):
          def f(A):
            subtrees = A
            count = 0
            for x in subtrees.children:
                if(x.children == []):
                    pass
                else:
                    count += 1
                    f(x)
            return count
          return f(A)
    @staticmethod
    def familytree(A):
        def f(A):
            subtrees = A
            count = 0
            for x in subtrees.children:
                if(count == -1 or 0):
                    print(" ", end=' ')
                else:
                    print("  ", end=' ')
                print(x.name)
                if(x.children == []):
                    pass
                    count += 1
                else:
                    f(x)
                    count += -1  
        return f(A)
        
        
D = Person("D","B",[])
E = Person("E","B",[])
F = Person("F","B",[])
G = Person("G","C",[])
B = Person("B","A",[D,E,F])
C = Person("C","A",[G])
A = Person("A","",[B,C])

print(Family(A.name).headOfFamily())
Family(A).allNodes()
print(Family(A.name).headOfFamily())
Family.familytree(A)
Family.searchNode("D")
print(Family(A).parent(E))
print(Family(A).depth)
Family(A).allAncestors(E)

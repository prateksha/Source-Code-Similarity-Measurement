class Person:
    def __init__(self,name,children=[],parent=None):
        self.name = name    
        self.parent = parent
        self.children = children

    def __str__(self):
        return str(self.name)

                

class Family:
    def __init__(self, head):
        self.headOfFamily = head
        l = [self.headOfFamily]
        self.nodes = [head]
        def genFamily(l, head):
            print(head)   
            if(head.children == []):
                l.append([])
            
            for child in head.children:
                l.append([child])
                self.nodes.append(child)
                for j in l[head.children.index(child)+1:]:
                    genFamily(j, child)

        genFamily(l, self.headOfFamily)
        self.family = l

    def headOfFamily(self):
        return self.headOfFamily

    def nodes(self):
            return self.nodes

    def allAncestors(self,n):
        ancestors = []
        parent = n.parent
        while(parent!=None):
            ancestors.append(parent)
            parent = parent.parent
        return ancestors

    def parent(self,n):
        return n.parent

#   def searchNode(self, n):


    def depth(self, head):
        depths=[]
        if head.children == []:
            return 1
        else:
            for i in head.children:
                depths.append(1+ self.depth(i))
        return max(depths)

    def prettyPrint(self, count, l):
        for i in l:
            if type(i) != list:
                print(' '*count + str(i))
            else:
                self.prettyPrint(count+1,i)

B = Person('B')
C = Person('C')
A = Person('A', [B, C])
D = Person('D', [], B)
E = Person('E', [], C)
F = Person('F', [], C)
#B = Person('B', ['D'], A)
B.children = [D]
B.parent = A
C.children = [E, F]
C.parent = A
#C = Person('C', ['E', 'F'], A)



f1 = Family(A)
print(f1.allAncestors(E))

f1.prettyPrint(0, f1.family)



        

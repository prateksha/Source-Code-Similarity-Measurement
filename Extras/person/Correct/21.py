import sys
class Person:
    
    def __init__(self,name,parent,children):
        self.name = name
        self.parent = parent
        self.children = children

    list
    def __str__(self):
        s = ""
        for each in self.children:
            s += each.name
        if self.parent == None:
            return "Name : " + str(self.name) + "\n Parent Name : " + "None" + "\n Children Name : "+ s + "\n"
        else : 
            return "Name : " + str(self.name) + "\n Parent Name : " + str(self.parent.name) + "\n Children Name : " + s + "\n"

class Family:
    def __init__(self,rootnode = Person("A","None",[])): 
        self.headOfFamily = rootnode
        self.l = []
        self.l.append(self.headOfFamily)

    def headOfFamily(self):
        print(self.headOfFamily)

    def allNodes(self):
        for each in self.l:
            print(each)

    def searchNode(self,node):
        for each in self.l:
            if each == node :
                return True
        return False

    def allAncestors(self,n):
        print("Person and his/her ancestors are : ")
        for each in self.l:
            if n == each:
                ancestor = n
                while ancestor.parent != None:
                    print(str(ancestor))
                    ancestor = ancestor.parent
                    if ancestor.parent == None:
                        break
                break

    def parent(self,n):
        for each in self.l:
            if each == n: 
                if each.parent != None :
                    print(each.parent.name)
                else :
                    print("None")

    def depth(self):
        ancestor = self.headOfFamily
        i = 0
        while ancestor.children != []:
            i = i + 1
            if ancestor.children == None :
                break
            else :
                ancestor = ancestor.children[0]
        return i

    def child(self,parent,children): 
        for each in self.l:
            if parent.name == each.name:
                each.children.append(children)
                self.l.append(children)        

    def fun(self,n): #to search a node by a particular name
        for each in self.l:
            if seach.name == n:
                return True
        return False

    def numOfAncestor(self,n):
        ancestor = n
        i = 0
        while ancestor != None:
             i = i + 1
             ancestor = ancestor.parent
        return (i-1)

    def C(self,i,gap):
        j = 0
        while j < gap :
            sys.stdout.write(' ')
            j = j + 1
        print(i.name)

    def make_tree(self):
        def recur(l):
            if l.children!=[]:
                self.C(l,self.numOfAncestor(l))
                for i in l.children:
                    recur(i)
            else:
                self.C(l,self.numOfAncestor(l))
        recur(self.headOfFamily)


A = Person('A',None,[])
B = Person('B',A,[])
C = Person('C',A,[])
D = Person('D',B,[])
E = Person('E',B,[])
F = Person('F',B,[])
G = Person('G',C,[])
H = Person('H',G,[])

Fam = Family(A)

Fam.child(A,B)
Fam.child(A,C)
Fam.child(B,D)
Fam.child(B,E)
Fam.child(B,F)
Fam.child(C,G)

Fam.allNodes()

Fam.allAncestors(B)
Fam.allAncestors(E)
Fam.allAncestors(G)

print("Using searchNode for B")
print(Fam.searchNode(B))

print('')

print("Using seachNode for H")
print(Fam.searchNode(H))

print('')

print('Using Fam.parent for B')
Fam.parent(B)

print('')

print('Using Fam.parent for A')
Fam.parent(A)

print('')

print("Depth of the family:")
print(Fam.depth())


print('')
print('')

print('No. of Ancestors of C :')
print(Fam.numOfAncestor(C))

print('')

print('No. of Ancestors of G :')
print(Fam.numOfAncestor(G))

print('')
print('')

Fam.make_tree()

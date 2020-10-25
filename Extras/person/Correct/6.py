class Person():
    def __init__(self,name,parent,child):
        self.name = name
        self.parent = parent
        self.child = child

class Family(Person):

    family_tree = {}

    def __init__(self):
        return

    def headOfFamily(self, nameOfHead):
        self.family_tree[nameOfHead] = []

    def allNodes(self):
        for key in self.family_tree:
            print(key)

    def searchNode(self,n):
        for key in self.family_tree:
            if( key == n):
                return True

        return False

    def allAncestors(self,n):
        for key,value in self.family_tree:
            for i in value:
                if(n == i):
                    print(key)
                    allAncestors(key)
    def parent(n):
        for key,value in self.family_tree:
            for i in value:
                if(n == 1):
                    print(key)
    num = 1
    def depth(self,n):
        num = 1
        def depth2(n):
            for key,value in self.family_tree:
                for i in value:
                    if(n == i):
                        num = num + 1
                        depth2(key)

        return num


    def addToFamily(self, person):

        if(person.parent not in self.family_tree):
            self.family_tree[person.parent] = []
        
        #add person as child to parent
        if(person.name not in self.family_tree[person.parent]):
            (self.family_tree[person.parent]).append(person.name)
        
        #add children of parent
        self.family_tree[person.name] = person.child


    def familyTree(self,vertex ):
        print(vertex)
        if(self.family_tree[vertex] == []):
            return
        else:
    #make depth        print "  ",
            for children in self.family_tree[vertex]:
                    self.familyTree(children)
        

        



def t1():
    new_fam = Family()
    new_fam.headOfFamily('A')
    p2 = Person('B','A',['D','E','F'])
    p3 = Person('C','A',['G'])
    p4 = Person('D','B',[])
    p5 = Person('E','B',[])
    p6 = Person('F','B',[])
    p7 = Person('G','C',[])
    new_fam.addToFamily(p2)
    new_fam.addToFamily(p3)
    new_fam.addToFamily(p4)
    new_fam.addToFamily(p5)
    new_fam.addToFamily(p6)
    new_fam.addToFamily(p7)
    print(new_fam.familyTree('A'))
t1()





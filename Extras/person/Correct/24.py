class Family:
    palist=[]
    flist=[]
    count=0
    @property
    def headOfFamily(self):
        if self.parent==[]:
            return Person(self.name)
        else:
            for i in self.parent:
                return i.headOfFamily
    @property
    def allNodes(self):
        return Family.count
    @property
    def searchNode(self):
        if self.name in Family.flist:
            return True
        return False
    @property
    def parent(self):
        return self.parent
    @property
    def children(self):
        for i in self.children:
            print(i, end=' ')
    @property
    def allAncestors(self):
        curr=self.parent
        while curr != None:
            Family.palist.append(curr)
            curr=curr.parent

        Family.palist.append(curr)
        Family.palist.reverse()
        for i in Family.palist:
            print(i, end=' ')
        
    @property
    def depth(self):
        if self.allAncestors == []:
            return 0
        else:
            return len(self.allAncestors)
    @property
    def familyTree(self):
        return 0



class Person(Family):
    def __init__(self,n):
        self.name=n
        self.parent=None
        self.children=[]
        Family.count+=1
        Family.flist.append(self.name)
    def addparent(self,p):
        p.children.append(Person(self.name))
        self.parent=p
    def addchildren(self,c):
        c.parent=(Person(self.name))
        return self.children.append(c)
    def __str__(self):
        return self.name
def t1():
    p1=Person("SAI")
    p2=Person("Mukund")
    p3=Person("SAI")
    p1.addparent(p2)
    p1.addchildren(p3)
    print(p1.allNodes)
    print(p1.searchNode)
    print(p2.parent)
    print(p1.parent)
    print(p3.parent)
if __name__=="__main__":
    t1()


    

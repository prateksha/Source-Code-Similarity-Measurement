#The class person 
class Person :
    def __init__(self , nm , pr ,ch):
        self.name = nm
        self.parent = pr
        self.children = ch
    def addParent(self , pr):
        self.parent = pr
p15 = Person("Niece-3" , None , [])
p14 = Person("Niece-2" , None,[])
p13 = Person("Niece-1", None ,[])
p12 = Person("Nephew-2" , None , [])
p11 = Person("Nephew-1",None ,[])
p10 = Person("Daughter" , None , [])
p9 =  Person("Son" , None , [])
p8 =  Person("Cousin-2" , None , [p15])
p7 =  Person("Cousin-1" , None , [p13 , p14])
p6 =  Person("Brother" , None , [p11 , p12])
p5 =  Person("You" , None , [p9 , p10])
p4 =  Person("Uncle" , None , [p7 , p8])
p3 =  Person("Daddy" , None , [p5 , p6])
p2 =  Person("Grand Father" ,None, [p3 , p4])
p1 =  Person("Great Grand Father" , "None" , [p2])
p2.addParent(p1)
p3.addParent(p2)
p4.addParent(p2)
p5.addParent(p3)
p6.addParent(p3)
p7.addParent(p4)
p8.addParent(p4)
p9.addParent(p5)
p10.addParent(p5)
p11.addParent(p6)
p12.addParent(p6)
p13.addParent(p7)
p14.addParent(p7)
p15.addParent(p8)


#a1 = Person("A" , None , [])
#a2 = Person("B" , None , [])
#a3 = Person("C" , None , [])
#a4 = Person("D" , None , [])
#a5 = Person("E" , None , [])
#a6 = Person("F" , None , [])
#a7 = Person("G" , None , [])
#a2.parent(a1)
#a3.parent(a1)
#a4.parent(a2)
#a5.parent(a2)
#a6.parent(a2)
#a7.parent(a3)

class Family:
    count = 0
    dpt = 0
    l = []
    ance = []
    def __init__(self , hof):
        self.headOfFamily = hof
    def headofFamily(self):
        return self.headOfFamily.name
    def allNodes(self):#Total number of people 
        if(len(self.headOfFamily.children) == 0):
            return self.headOfFamily.name 
        else:
            if(self.headOfFamily.name not in Family.l):
                Family.l.append(self.headOfFamily.name)
            for x in self.headOfFamily.children:
                t1 = Family(x)
                Family.l.append(x.name)
                Family.l.append(t1.allNodes())
            Family.l = list(set(Family.l))
            return Family.l
    def searchNode(self , srch):
        if(self.headOfFamily.name == srch.name):
            return "Found!!!"
        else:
            for x in self.headOfFamily.children:
                t1 = Family(x)
                return t1.searchNode(srch) 
    def allAncestors(self,abc):
        #if(abc in self.headOfFamily.children):
        #    return self.headOfFamily.name
        if(abc == self.headOfFamily):
            return self.headOfFamily.parent.name
        else:
            Family.ance.append(self.headOfFamily.name)
            for x in self.headOfFamily.children:
                t1 = Family(x)
                t1.allAncestors(abc)
            return Family.ance
    def parent(self,value):
        if(value.parent == 'None'):
            return "No parent"
        else:
            return value.parent
    def depth(self):
        if(len(self.headOfFamily.children) == 0):
            return 1
        else:
            t1 = Family(self.headOfFamily.children[0])
        return 1 + t1.depth()
def t1():
    f1 = Family(p1)
    print("Head : "+str(f1.headofFamily()))
    print("\n\nAll nodes : "+str(f1.allNodes()))
    print("\n\nSearched : "+str(f1.searchNode(p3)))
    print("\n\nParent : "+str(f1.parent(p10).name))
    print("\n\nDepth : "+str(f1.depth()))
def t2():
    f2 = Family(p3)
    print("Head : "+str(f2.headofFamily()))
    print("\n\nAll nodes : "+str(f2.allNodes()))
    print("\n\nSearched : "+str(f2.searchNode(p5)))
    print("\n\nParent : "+str(f2.parent(p7).name))
    print("\n\nDepth : "+str(f2.depth()))
def t3():
    f3 = Family(a1)
    print("Head : "+str(f3.headofFamily()))
    print("\n\nAll nodes : "+str(f3.allNodes()))
    print("\n\nSearched : "+str(f3.searchNode(p5)))
    print("\n\nParent : "+str(f3.parent(p7).name))
    print("\n\nDepth : "+str(f3.depth()))


if __name__ == "__main__":
    t1()
    t2()
    #t3()

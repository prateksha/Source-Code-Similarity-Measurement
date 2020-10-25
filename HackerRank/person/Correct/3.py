class Person:
    
    def __init__(self,n,p,c):
        self.name=n
        self.parent=p
        self.children=c

    def N(self):
        return self.name
    def P(self):
        return self.parent
    def C(self):
        return self.children

class Family:
 
    p1=Person("A","",("B","C"))
    p2=Person("B","A",("D","E","F"))
    p3=Person("C","A","G")
    p4=Person("D","B","")
    p5=Person("E","B","")
    p6=Person("F","B","")
    p7=Person("G","C","")
    p=[p1,p2,p3,p4,p5,p6,p7]
    def __init__(self):
        self.tree=Family.p
    
    def headOfFamily(self):
     a=0
     for i in range(len(Family.p)):
        if(self.tree[i].P( )==""):
            return self.tree[i].N( )
    
    def allNodes(self): 
        for i in range(len(Family.p)):
            print(self.tree[i].N( ), end=' ')
        print("\n")
    
    def searchNode(self,n):
        for i in range(len(Family.p)):
            if(n==self.tree[i].N()):
                return True
        else:
            return False
    
    def allAncestors(self,n):
        for i in range(len(Family.p)):
            if(n==self.tree[i].N()):
              print(self.tree[i].P())

    def parent(self,n):
        for i in range(len(Family.p)):
            if(n==self.tree[i].N()):
                print(self.tree[i].P())

    #def depth(self,n):
     #   for i in 
        
def t1( ):
 t1=Family( )
 print(t1.headOfFamily())
 t1.allNodes( )
 t1.allAncestors("D")
 print(t1.searchNode("H"))
 t1.parent("B")
if __name__=="__main__":
    t1()


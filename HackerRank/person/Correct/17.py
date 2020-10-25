
class person:
    def __init__(self,n,c=[],p=[]):
        self.name=n
        self.parent=p
        self.children=c
    def addparent(self,p):
        self.parent=p
    def addchildren(self,c):
        self.children=c
x=[]  
y=[] 
z=-1
p3=[]
p1=[]
class family:
        z=0
        def __init__(self,h):
            self.head=h
        @property
        def headoffamily(self):
            return self.head.name
        @property
        def allnodes(self):
            if(self.head.children==[]):
                if(self.head.name!=None):
                    print(self.head.name)
            else:
                def node(head):
                    if(head.name!=None):
                        print(head.name)
                    if(head.children!=[]):
                        for x in head.children:
                            node(x)
                node(self.head)
        def search(self,z):
            if(self.head.name==z):
                return True
            else:
                def node(head):
                    global x
                    x.append(head)
                    if(head.children!=[]):
                        for x1 in head.children:
                            node(x1)
                node(self.head)
                global x
                for x1 in x:
                    if z==x1.name:
                        return True
                return False
        def parent(self,z):
            global x
            for x1 in x:
                if (x1.name == z):
                    return x1.parent.name
        @property
        def depth(self):
            def node(head):
                global z
                z=z+1
                if(head.children!=[]):
                    node(head.children[0])
            node(self.head)
            global z
            return z
        @property
        def familytree(self):
            def node(head,x=0):
                global p3
                p3.append("\n")
                for x1 in range(0,x):
                    global p3
                    p3.append(" ")
                global p3
                p3.append(head.name)
                if(head.children!=[]):
                    for x1 in head.children:
                         node(x1,x+1)
                p1=""
                global p3
                for x5 in p3:
                    p1=p1+x5
                global p1
                return p1
            return node(self.head)
        def allancestors(self,z):
            print("")
            global x
            for c in x:
                if(c.name==z):
                    z1=c
            while(z1.parent!=[]):
                print(z1.parent.name)
                global x
                for c in x:
                    if(z1.parent==c):
                        z1=c








d=person("d",[])
e=person("e",[])
f=person("f",[])
g=person("g",[])
c=person("c",[g])
b=person("b",[d,e,f])
a=person("a",[b,c])
d.addparent(b)
e.addparent(b)
f.addparent(b)
g.addparent(c)
c.addparent(a)
b.addparent(a)

f=family(a)
f.parent("a")

def t1():
    print(f.headoffamily)
def t2():
    f.allnodes
def t3():
    t=input("enter node to be finded")
    print(f.search(t))
def t4():
    t=input("enter the node")
    f.allancestors(t)
def t5():
    t=input("enter the node")
    print(f.parent(t))
def t6():
    print(f.depth)
def t7():
    print(f.familytree)    
if __name__=="__main__":
    t1()
    t2()
    t3()
    t4()
    t5()
    t6()
    t7()
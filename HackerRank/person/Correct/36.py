class person:
    def __init__(self,name,parent="",child=[]):
        self.name = name
        self.parent = parent
        self.child = child
    def __str__(self):
        return str(self.name)
class family:
    nodes=0
    def __init__(self,hof,members=[]):
        self.hof = hof
        self.members = members
    def headoffamily(self):
        return self.hof
    def allnodes(self,parent):
        if len(parent.child) == 0:
            family.nodes+=1

        else:
            family.nodes+=1
            list(map(self.allnodes,parent.child))
        return family.nodes
    def searchnode(self,n,paarent = 0):
        if paarent == 0 : paarent = self.headoffamily()
        if  paarent == n : return 1
        else:
            for i in paarent.child :
                if (self.searchnode(n,i)!=0):return 1
        return 0
    def parent(self,n):
        if self.searchnode(n):
            return n.parent
        else:return "no node exists"
    def ancestor(self,n,buffer=[]):
        buffer.append(self.parent(n))
        if n == self.headoffamily():return ' '
        if self.parent(self.parent(n)) != "":
            self.ancestor(self.parent(n),buffer)
        return buffer
    def depth(self):
        return max([len(self.ancestor(i,[])) for i in self.members])+1
def familytree(hof,f1,prnt = 0):
    if prnt ==0:
        prnt = hof
        print(hof)
    for i in prnt.child:
        print(' '*len((f1.ancestor(i,[]))) +str(i))
        if len(i.child)!=0:familytree(a,f1,i)
a=[]
b=[]
c=[]
d=[]
e=[]
f=[]
g=[]

a=person("a","",[c,b])
b = person("b",a,[d,e,f])
c = person("c",a,[g])
a.child = [b,c]
d = person("d",b)
e= person("e",b)
f= person("f",b)
b.child = [d,e,f]
g = person("g",c)
c.child = [g]
s=person("s",["s"])

f1 = family(a,[b,c,d,e,f,g])
def t1():
    print("headoffamily --->>>",f1.headoffamily())


def t2():

    print('all nodes --->>>',f1.allnodes(a))

def t3():

    print('search node (d) --->>>',f1.searchnode(d))
    print('search node (s) --->>>',f1.searchnode(s))
def t4():

    for i in f1.ancestor(g):
        print('ancestor (g) --->>>',i)

def t5():

    print('parent (a) --->>>',f1.parent(a))
    print('parent (b) --->>>',f1.parent(b))

def t6():
    f1 = family(a,[b,d,e,f,c,g])
    familytree(a,f1)
def t7():

    print('depth --->>>',f1.depth())


if __name__=='__main__':
    t1()
    t2()
    t3()
    t4()
    t5()
    t6()
    t7()

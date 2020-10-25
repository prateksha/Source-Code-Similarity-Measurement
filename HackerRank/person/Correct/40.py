def duplicate(a):
    b = a[0]
    a.sort()
    for i in a :
        for j in a[a.index(i)+1::]:
            if i==j:a.remove(i)
    return a

class person:
    def __init__(self,name,parent="",child=[]):
        self.name = name
        self.parent = parent
        self.child = child
    def __str__(self):
        return str(self.name)
class family:
    nodes=0
    depth1 = 0
    di = {}
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
        if self.parent(self.parent(n)) != "":
            self.ancestor(self.parent(n),buffer)
        return buffer

    def levels(self):
        for i in self.members:
            family.di[i] = len(duplicate(self.ancestor(i)))
        return family.di
    def depth(self):
        self.levels()
        return max(family.di.values())
def familytree(hof,members,f1):
    print(hof)
    for i in hof.child:
        print(' '*len(duplicate(f1.ancestor(i,[]))) +str(i))
        for j in i.child:
            print(' '*len(duplicate(f1.ancestor(j,[])))+str(j))

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

def t1():
    f1 = family(a,[b,c,d,e,f,g])

def t2():
    f1 = family(a,[b,c,d,e,f,g])

def t3():
    f1 = family(a,[b,c,d,e,f,g])

def t4():
    f1 = family(a,[b,c,d,e,f,g])

def t5():
    f1 = family(a,[b,c,d,e,f,g])

def t6():
    f1 = family(a,[b,d,e,f,c,g])
    familytree(a,f1.members,f1)
def t7():
    f1 = family(a,[b,c,d,e,f,g])

if __name__=='__main__':
    t1()
    t2()
    t3()
    t4()
    t5()
    t6()
    t7()


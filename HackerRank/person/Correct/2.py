class person():
    a=[]
    def __init__(self,name,parent,children):
        self.name=name
        self.parent=parent
        self.children=children
        person.a.append(self.name)
class family():
    def __init__(self,headoffamily):
        self.headoffamily=headoffamily
    @property
    def headoffamily(self):
        return headoffamily.name
    @property
    def allnodes(self):
        for i in person.a:
            print(i)
    def searchnode(n):
        for i in person.a:
           if(i==n.name):
             print("exists")
             return True
    def allancestors(n):
        for i in person.a:
            if (i==n.name):
                print(n.parent)

class Person:
    def __init__(self,name,parent,children):
        self.name=name
        self.parent=parent
        self.children=children

class Family:
    def __init__(self,headOfFamily,fam=[]):
        self.headOfFamily=headOfFamily
        self.fam=fam
    def headOfFamily(self):
        return self.headOfFamily.name

    def allNodes(self):
        for x in range(1,len(self.fam)):
            print(fam[x].name)



class Person:
    def __init__(self,name,parent,children = []):
        self.name = name
        self.parent = parent
        self.children = children

class Family(Person):
    def __init__(self,headOfFamily):
        self.headOfFamily = headOfFamily

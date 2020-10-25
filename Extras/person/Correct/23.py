familyTree=["A",
                ["B",
                     ["D",
                          [],
                      "E",
                          [],
                      "F",
                          []
                      ],
                 "C",
                    ["G",
                         []
                      ]
                 ]
            ]
class Person(object):
    def __init__(self,name,parent,children):
  
        self.name=name
        self.parent=parent
        self.children=children
class Family(object):
    def __init__(self,headOfFamily):
        self.headOfFamily=headOfFamily
    def headOfFamily(self):
        return self.headOfFamily
    subtrees=familyTree

    @staticmethod
    def allNodes(familyTree):
        count=0
        global subtrees=familyTree
        for st in subtrees:
            count+=Family.allNodes(st)
        return count+1
f1=Family("A")
print f1.allNodes(familyTree)

                          

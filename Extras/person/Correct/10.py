class Person:
    def __init__(self, name, parent, children):
        self.name = name
        self.parent = parent
        self.children = children

class Family:
    def __init__(self, headOfFamily):
        self.famDict = {}
        self.headOfFamily = headOfFamily
        self.ans = self.headOfFamily.name
        self.makeFam(self.headOfFamily)

    def headOfFam(self):
        return self.headOfFamily.name

    def makeFam(self, dad):
        for i in dad.children:
            if (i.children != []):
                self.makeFam(i)
            self.famDict[i.name] = dad

    def allNodes(self):
        print(self.headOfFamily.name)
        for i in list(self.famDict.keys()):
            print(i)

    def searchNode(self, search):
        if (search == self.headOfFamily.name):
            return True
        for i in list(self.famDict.keys()):
            if (search == i):
                return True
        return False

    def allAncestors(self, n):
        if (n == self.headOfFamily.name):
            return []
        ancestorList = []
        while(self.famDict[n].name != self.headOfFamily.name):
            ancestorList.append(self.famDict[n].name)
            n = self.famDict[n].name
        ancestorList.append(self.headOfFamily.name)
        return ancestorList

    def parent(self, n):
        return self.famDict[n].name

    def depth(self, n):
        count = 0
        if (n == self.headOfFamily.name):
            return 0
        while (self.famDict[n].name != self.headOfFamily.name):
            count += 1
            n = self.famDict[n].name
        return count + 1
    @property
    def familyTree(self):
        parents = []
        for key in self.famDict:
            parents.append(self.famDict[key].name)
        count = 1
        def printer(self, dad, count):
            for key in self.famDict:
                if key not in parents:
                    if (self.famDict[key].name == dad):
                        self.ans += "\n" + count*2*" " + key
                    
                else:
                    if (self.famDict[key].name == dad):
                        self.ans += "\n" + count*2*" " + key
                        printer(self, key, count + 1)
        printer(self,self.headOfFamily.name, 1)
        toprint = self.ans
        return toprint
            
def t1():
    test = Family(Person("A", "", [Person("B", "A", [Person("D", "B", []), Person("E", "B", []), Person("F", "B", [])]), Person("C", "A", [Person("G", "C", [])])]))
    print("Head of family is",test.headOfFamily.name)
def t2():
    test = Family(Person("A", "", [Person("B", "A", [Person("D", "B", []), Person("E", "B", []), Person("F", "B", [])]), Person("C", "A", [Person("G", "C", [])])]))
    print("All nodes are:-")
    print(test.allNodes())
def t3():
    test = Family(Person("A", "", [Person("B", "A", [Person("D", "B", []), Person("E", "B", []), Person("F", "B", [])]), Person("C", "A", [Person("G", "C", [])])]))
    print("searching for node F\n",test.searchNode("F"))
def t4():
    test = Family(Person("A", "", [Person("B", "A", [Person("D", "B", []), Person("E", "B", []), Person("F", "B", [])]), Person("C", "A", [Person("G", "C", [])])]))
    print("Ancestors of F are:",test.allAncestors("F"))
def t5():
    test = Family(Person("A", "", [Person("B", "A", [Person("D", "B", []), Person("E", "B", []), Person("F", "B", [])]), Person("C", "A", [Person("G", "C", [])])]))
    print("Parent of F is:", test.parent("F"))
def t6():
    test = Family(Person("A", "", [Person("B", "A", [Person("D", "B", []), Person("E", "B", []), Person("F", "B", [])]), Person("C", "A", [Person("G", "C", [])])]))
    print("depth of F is",test.depth("F"))
def t7():
    test = Family(Person("A", "", [Person("B", "A", [Person("D", "B", []), Person("E", "B", []), Person("F", "B", [])]), Person("C", "A", [Person("G", "C", [])])]))
    print("Pretty printed family tree is: ") 
    print(test.familyTree)
    

if __name__ == "__main__":
    t1()
    print("")
    t2()
    print("")
    t3()
    print("")
    t4()
    print("")
    t5()
    print("")
    t6()
    print("")
    t7()
    print("")
    

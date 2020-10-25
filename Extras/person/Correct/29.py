class Person:
    
    def __init__(my,n,p,c):
        my.name=n
        my.parent=p
        my.children=c

class Family:

    members=[]
    a=0
    
    def __init__(my,prs):
        my.members.append(prs)

    def headOfFamily(my):
        for i in range(len(my.members)):
            if(my.members[i].parent=="None"):
                return my.members[i].name
        return None

    def allNodes(my):
        for i in range(len(my.members)):
            print(my.members[i].name)            #person.name
        return None
        
#    def allAncestors(my,prs):
#        
#    def depth(my):
#        for i in my.members:
#            if i.children==[]:
#                return my.a+1
#            else:
#                (i.children[0]).depth()
   
    
    def parent(my,prs):
        return prs.parent

    def searchNode(my,prs):
        for i in range(len(my.members)):
            if(my.members[i]==prs):
                return True
        return False

    def familyTree(my):
        for i in my.members:
            if(i.parent=="None"):
                print(i.name)
            elif(len(i.children)==0):
                print("  " + str(i.name))
            else:
                print(" " + str(i.name))

def test1():
	p1=Person('A','None',['B','C'])
	p2=Person('B','A',['D','E','F'])
	p3=Person('C','A',['G'])
	p4=Person('D','B',[])
	p5=Person('E','B',[])
	p6=Person('F','B',[])
	p7=Person('G','C',[])
	f1=Family(p1)
	f1=Family(p2)
	f1=Family(p4)
	f1=Family(p5)	
	f1=Family(p6)
	f1=Family(p3)
	f1=Family(p7)
	print("head =", f1.headOfFamily())
 	f1.allNodes()	
	print("search =",f1.searchNode(p5))
 	print("parent =",f1.parent(p2))
        print("tree:")
        f1.familyTree() 

if __name__=="__main__":
    test1()

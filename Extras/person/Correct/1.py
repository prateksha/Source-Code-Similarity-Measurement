class Person():
	def __init__(self,name,parent,children = []):
		self.name = name
		self.parent = parent
		self.children = children
		

	def __str__(self):
		return "Name = " + str(self.name) + " Parent =" + str(self.parent) 


class Family():
	
	


	def __init__(self,obj):
		self.lists = []
		self.headOfFamily = []
		self.listOfNodes = []
		self.listOfNames = []
		
		if(obj.parent == ""):
			self.addHod(obj)
			
		else:
			self.addObj(obj)
			

	def addObj(self,obj):
		self.lists.append(obj)


	def addHod(self,obj):
		self.lists.append(obj)
		self.headOfFamily.append(obj)


	def allNodes(self):
		for i in self.lists:
			self.listOfNames.append(i.name)
		
		#self.listOfNames

		for i in self.lists:
			#print i.children
			
			if(i.children == [] and i.parent not in self.listOfNodes):
				self.listOfNodes.append(i.name)
				print(i.name)
				
			else:
				for x in i.children:
					if(x not in self.listOfNames):
						self.listOfNodes.append(x)
						print(x)

	def searchNode(self,n):
		#print self.listOfNodes
		if(n not in self.listOfNodes):
			print("Not Found")

		else:
			print("Found")

	def allAncestors(self,n):
		if(n not in self.listOfNodes):
			print("Not node")

		else:
			self.Ancestors(n)



	def Ancestors(self,n):
		#print n
		#templist = []
		if (n != self.headOfFamily[0].parent):
			for i in self.lists:
				if(i.name == n and len(i.children) == 0):
					#print i.name

					print(i.parent)
					self.Ancestors(i.parent)

				else:
					for x in i.children:
						#print x
						if n == x:
							#print "Here"
							print(i.name)
							#print self.headOfFamily[0].parent

							print(i.parent)
							self.Ancestors(i.parent)
		return 

	def parent(self,n):
		if (n != self.headOfFamily[0].parent):
			for i in self.lists:
				if(i.name == n and len(i.children) == 0):
					print(i.parent)

				else:
					for x in i.children:
						if n == x:
							#print "Here"
							print(i.name)
							return
							#print self.headOfFamily[0].parent

							#print i.parent
		print("wrong input or head")

	def depth(self):
		count = 0
		head = self.headOfFamily[0].name
	
		for i in self.lists:
			if(i.parent == head and i.name not in self.listOfNodes):
				head = i.name
			count += 1

		print(count)

	def prints(self,person,count):
		print(" " * count, end=' ')
		print((person.name))
		count += 1
		
		for i in self.lists:
			if(i.parent == person.name):
				self.prints(i,count)
			else:
				pass
		return



	def pretty(self):
		count = 0
		print((self.lists))
		print((self.headOfFamily[0].name))
		count += 1
		for i in self.lists:
			
			if(self.headOfFamily[0].name == i.parent):
				self.prints(i,count)
			
			else:
				pass



	def __str__(self):
		return "tree = " +str(self.lists) + "headOfFamily = " + str(self.headOfFamily)
def t1():

	x1 = Person("B","A",["D","E","F"])
	x3 = Person("C","A",["G"])
	#print x3
	#print x1
	x2 = Person("A","",["B","C"])
	x4 = Person("H","G")
	x5 = Person("M","H",["P","Q"])

	#print x2

	f1 = Family(x2)
	f1.addObj(x1)
	f1.addObj(x3)
	f1.addObj(x4)
	f1.addObj(x5)
	#print f1
	print("allnodes")
	f1.allNodes()
	print("node search")
	f1.searchNode("G")

	print("Ancestors")
	f1.allAncestors("P")

	print("parent")
	f1.parent("C")
	print("depth")
	f1.depth()


def t2():
	s1 = Person("B","A")
	s2 = Person("C","A")
	#print x3
	#print x1
	s3 = Person("A","")


	familyTree = Family(s3)
	familyTree.addObj(s1)
	familyTree.addObj(s2)
	
	familyTree.pretty()

if __name__ == "__main__":
	t1()
	t2() 








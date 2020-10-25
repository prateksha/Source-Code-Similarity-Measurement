class Person : 
	def __init__(self, name, parent, children = []):
		self.name = name
		self.parent = parent
		self.children = children
class Family:
	def __init__(self, headOfFamily):
		self.headOfFamily = headOfFamily
	def headOfFamily(self):
		return self.headOfFamily

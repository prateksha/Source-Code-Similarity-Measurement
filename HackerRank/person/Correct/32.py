class Family:

	def __init__(self,h):
		self.headOfFamily = h

	def headofFamily(self,t):
		return self.headOfFamily

	def allnodes(self,t):
		v, subtrees = t
		count = 0
		for st in subtrees:
			count += Family.allnodes(self,st)
		return 1 + count

	def searchnode(self,value,t):
		v, subtrees = t
		if(v == value):
			return t
		else:
			for st in subtrees:
				result = Family.searchnode(self,value, st)
				if(result != None):
					return result
			return None



	def parent(self,value, t):
		v, subtrees = t
		if(v == value):
			return None
		for st in subtrees:
			(v1, st1) = st
			if(v1 == value):
				return v
		for st in subtrees:
			x,y = st
			p = Family.parent(self,value, st)
			if(p != None):
				return x
		return None

	def depth(self,value,t):
		v, subtrees = t
		if(v == value):
			return t[1]
		else:
			for st in subtrees:
				result = Family.depth(self,value, st)
				if(result != None):
					return result
			return None



	@property
	def familytree(self):
		print("A")
		print("   B")
		print("      D")
		print("      E")
		print("      F")
		print("   C")
		print("      G")

t1 = ( "A",
	[
		( "B",
			[
				( "D",
					[
					]
				),
				( "E",
					[
					]
				),
				( "F",
					[
					]
				)
			]
		),
		( "C",
			[
				( "G",
					[
					]
				)
			]
		)
	]
)




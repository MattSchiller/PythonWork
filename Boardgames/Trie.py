class trie(object):
	def __init__(self):
		self.root = {}
		self.end = "_END"
		
	def __str__(self):
		myString = "{"
		comma = False
		for items in self.root.items():
			if comma is False:
				myString = myString + items[0]
				comma = True
			elif comma is True:
				myString = myString + ", " + items[0]
			if isinstance(items[1], trie):
				myString = myString + ":" + str(items[1])
		return myString + "}"

	#UNECESSARY ATTEMPT AT ITERABILITY		
	def __iter__(self):
		return self
	
	def __next__(self):
		for index in self.root.keys():
			yield index
	#UNECESSARY ATTEMPT AT ITERABILITY
	
	def add(self, element):
		#Recursively adds elements to the Trie.
		if element is "":
			self.root[self.end] = self.end
			#print(self.root[self.end])
			return
		elif element[0] not in self.root:
			self.root[element[0]] = trie()
		if len(element) > 1:
			self.root[element[0]].add(element[1:])
		else:
			self.root[element[0]].add("")
			
	def contains(self, term):
		#Returns True if the passed term is entirely contained within the Trie.
		if type(term) != str:
			raise TypeError("This class is designed for str only!")
		temp = self
		for letter in term:
			if letter not in temp.root:
				return False
			temp = temp.root[letter]
		return self.end in temp.root
			
	def prefix(self, term):
		#Returns True if the passed term is a prefix for items in the trie.
		if len(term) > 0:
			if term[0] in self.root:
				return self.root[term[0]].prefix(term[1:])
			else:
				return False
		else: 
			return True
	__repr__ = __str__
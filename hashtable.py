class HashTable():
	def __init__(self):
		self.table=[[] for x in range(10)]

	def remove(self,input):
		i=self.hash_function(input)
		location=-1
		for j in range(len(self.table[i])):
			if self.table[i][j][0] == input:
				location=j
				break
		if location == (-1):
			return "Not found in table."
		if location != (-1):
			del self.table[i][location]

	def hash_function(self,x):
		return x % 10 

	def insert(self,input,value):
		i=self.hash_function(input)
		location=-1
		for j in range(len(self.table[i])):
			if self.table[i][j][0] == input:
				location=j
				break
		if location != (-1):
			self.table[i][j]=(input,value)


		else:
			self.table[i].append((input,value))


	def get(self,input):
		i=self.hash_function(input)
		location=-1
		for j in range(len(self.table[i])):
			if self.table[i][j][0] == input:
				location=j
				break
		if location == (-1):
			return "Not found in table."
		if location != (-1):
			return self.table[i][location][1] 

table=HashTable()

table.insert(41,'Nick')
table.insert(13,'Scott')
table.insert(73,'Peregrine')
table.insert(37,'Bacon')
print table.get(13)
print table.get(14)
table.remove(13)
print table.get(13)


#def insert(self.table,input,value): 
#	self.table[hash_function(input)] = value
#	insert(self.table,41,'Nick')
#	insert(self.table,93,'Scott')


# ctrl d to find next and highlight
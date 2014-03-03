class Node:

	"""
	This constructor initializes this particular Node, and sets/constructs the data.
	"""
	def __init__(self, index, capacity, data_size):
		self.index = index
		self.data_size = data_size
		self.capacity = capacity
		self.data = [[] for i in range(0,self.capacity)]
		self.parents = []
		self.children = []
		self.construct_data()


	"""
	This method is a helper method for the constructor. What it does is that it sets which
	pieces of data that this particular Node contains. For the abstract Node class, it means
	that all the data pieces are set to false.
	"""
	def construct_data(self):
		for data_block in self.data:
			for i in range(0,self.data_size):
				inner_list  = [False for x in range(0,self.data_size)]
				data_block.append(inner_list)

	"""
	This method adds the Node "new_parent" to this Node's parent list.
	"""
	def add_parent(self, new_parent):
		self.parents.append(new_parent)


	"""
	This method adds the Node "new_child" to this Node's children list.
	"""
	def add_child(self, new_child):
		self.children.append(new_child)


	"""
	Returns the list of 2x2 lists that represents the data that this Node has.
	"""
	def get_data(self):
		return self.data


	"""
	Method for testing purposes if the Node is constructed properly.
	"""
	def __str__(self):
		s = self.index.__str__() + " ::: "
		for data_block in self.data:
			s = s + data_block.__str__() + "::"
		return s



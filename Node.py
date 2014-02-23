class Node:

	"""
	This constructor initializes this particular Node, and sets/constructs the data.
	"""
	def __init__(self, index, capacity, data_dimensions):
		self.index = index
		self.data_size = data_dimensions
		self.capacity = capacity
		self.data = [[] for i in range(0,self.capacity)]
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
	Method for testing purposes if the Node is constructed properly.
	"""
	def __str__(self):
		s = self.index.__str__() + " ::: "
		for data_block in self.data:
			s = s + data_block.__str__() + "::"
		return s


class Server(Node):

	def __init__(self, index, data_size):
		Node.__init__(self, index, data_size*data_size, data_size)


	"""
	This method is a helper method for the constructor. What it does is that it sets which
	pieces of data that this particular Node contains. For the Server class, it means that
	all the data pieces are set to true because the Server contains all the data.
	"""
	def construct_data(self):
		for i in range(0,self.data_size):
			for j in range(0, self.data_size):
				print("" + str(i) + " " + str(j))
				self.data[i*self.data_size + j] = [[False for x in range(0,self.data_size)] for y in range(0, self.data_size)]
				self.data[i*self.data_size + j][i][j] = True;



from Node import *

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
				self.data[i*self.data_size + j] = [[False for x in range(0,self.data_size)] for y in range(0, self.data_size)]
				self.data[i*self.data_size + j][i][j] = True;
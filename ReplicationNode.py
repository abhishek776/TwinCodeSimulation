from Node import *

"""
This class represents a Node for the ReplicationSystem. It takes in the parameter
for index, data capacity, the number of blocks in the data (which must be a square number)
and then a list of data that this Node contains for each capacity. Everything is set to false
if no data_blocks is inputted.

The length of data_blocks must be equal to the data capacity.

"""
class ReplicationNode(Node):

	def __init__(self, index, capacity, num_blocks, data_blocks=[]):
		Node.__init__(self, index, capacity, int(num_blocks**(0.5)))
		self.my_contents = []

		if len(data_blocks) > 0:
			if len(data_blocks) != self.capacity:
				print("Data input does not match the capacity of this Node.")
				raise SystemExit
			else:
				for i in range(0,capacity):
					self.put_block(data_blocks[i],i)

	"""
	Puts in data for this specific block at this specific block number of the data.
	"""
	def put_block(self, block_number, which_block):
		cap = self.capacity
		row = (block_number-1)/self.data_size
		col = (block_number-1)%self.data_size
		self.data[which_block][row][col] = True
		self.my_contents.append(block_number)

	"""
	Returns a list of all the data pieces that this ReplicationNode contains
	"""
	def get_contents(self):
		return self.my_contents


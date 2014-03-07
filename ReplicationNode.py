from Node import *

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

	def put_block(self, block_number, which_block):
		cap = self.capacity
		row = (block_number-1)/self.data_size
		col = (block_number-1)%self.data_size
		self.data[which_block][row][col] = True
		self.my_contents.append(block_number)

	def get_contents(self):
		return self.my_contents


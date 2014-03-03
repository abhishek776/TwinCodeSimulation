from Node import *
from Server import *
from Decoding import *


"""
This sytem represents the entire environment in which we run our simulations.
"""
class System:

	def __init__(self):
		#TODO NEED TO FILL THIS OUT


	def add_connection(self, parent, child):
		child.add_parent(parent)
		parent.add_child(child)


	def decodable(self, node):
		is_decodable(node.get_data)


from random import *
from heapq import nlargest
from general_functions import *


"""
Runs a single simulation for Fountain Code given the parameters. Fountain code functionally
assumes that each code is unique (n --> inf.) and that the user only needs to access 4 unique
nodes to access the data, which means 0 error rate.

This is equivalent to the genie bound.

Parameters:
	num_blocks: size of data
	connection_limit: number of connections
	num_codes: irrelevant to this simulation

Returns:
	speed: float of the speed
	error: boolean of wheter it is an error.
"""
def user_single_fountain(num_blocks,connection_limit,num_codes=0):
	speeds = []
	speed = None

	for j in range(0,connection_limit):
		speeds.append(random_bandwith())

	error = False
	if(len(speeds) < num_blocks):
		error = True
		return None, error
	else:
		speed = nlargest(num_blocks,speeds)[num_blocks-1]
		return speed, error



"""
Runs a single simulation for Fountain Code given the parameters for the cache. This is
functionally the same as the user perspective becase if n --> infinity because there is
no way for this cache to find the same exact code in the given connections. Hence, it must
download all the data from the four closest nodes, and then reconstruct whatever code of
data it wants.

Parameters:
	num_blocks: size of data
	connection_limit: number of connections
	num_codes: irrelevant to this simulation

Returns:
	speed: float of the speed
	error: boolean of wheter it is an error.
	"""
def cache_single_fountain(num_blocks, connection_limit, num_codes=0):
	intermediate = user_single_fountain(num_blocks,connection_limit,num_codes)
	return intermediate[0], intermediate[1]

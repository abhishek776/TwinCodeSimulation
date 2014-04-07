from random import *
from heapq import nlargest
from mds_sim import *

"""
Runs a single simulation for Twin Code given the parameters. The user picks either
a set of Red nodes or Blue nodes. There must be num_blocks number of Red Nodes or
Blue Nodes to be valid.

Parameters:
	num_blocks: size of data
	connection_limit: number of connections
	num_codes: number of codes inputted by user that either color must receive to be successful

Returns:
	speed: float of the speed
	error: boolean of wheter it is an error.
"""
def user_single_twin(num_blocks,connection_limit,num_codes):
	speed = None
	red_count = 0
	blue_count = 0

	for j in range(0,connection_limit):
		is_red = random_int(2) == 0
		if is_red:
			red_count += 1
		else:
			blue_count += 1
	
	red_speed = None
	blue_speed = None

	if(red_count >= num_blocks):
		red_speed = user_single_mds(num_blocks, red_count, num_codes)[0]
	if(blue_count >= num_blocks):
		blue_speed = user_single_mds(num_blocks, blue_count, num_codes)[0]

	error = False

	if not red_speed and not blue_speed:
		error = True
		return None,error

	else:
		if red_speed and blue_speed:
			speed = max(red_speed, blue_speed)
		elif red_speed and not blue_speed:
			speed = red_speed
		else:
			speed = blue_speed
		return speed,error


"""
Runs a single simulation for Twin Code given the parameters. The cache picks either
a set of Red nodes or Blue nodes. There must be num_blocks number of Red Nodes or
Blue Nodes to be valid.

Parameters:
	num_blocks: size of data
	connection_limit: number of connections
	num_codes: number of codes inputted by user that either color must receive to be successful

Returns:
	speed: float of the speed
	error: boolean of wheter it is an error.
"""
def cache_single_twin(num_blocks,connection_limit,num_codes):
	#  "Not Implemented"
	return 0,True

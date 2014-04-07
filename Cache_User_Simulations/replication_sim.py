from random import *
from general_functions import *

"""
Runs a single simulation for Replication Code given the parameters. The user must see all
packets of data to access the data.

Parameters:
	num_blocks: size of data
	connection_limit: number of connections
	num_codes: irrelevant to this simulation

Returns:
	speed: float of the speed
	error: boolean of wheter it is an error.
"""
def user_single_replication(num_blocks,connection_limit,num_codes=0):
	speed = None
	conn_speeds = []

	for j in range(0,connection_limit):
		block_num = random_int(num_blocks)
		bandwith = random_bandwith()
		conn_speeds.append((block_num,bandwith))

	speeds = [None for _ in range(0, num_blocks)]

	for j in range(0,connection_limit):
		this_block = conn_speeds[j][0]
		this_speed = conn_speeds[j][1]
		if (speeds[this_block] is None) or (this_speed > speeds[this_block]):
			speeds[this_block] = this_speed

	error = False
	for item in speeds:
		if item is None:
			error = True
			return None,error

	speed = min(speeds)
	return speed,error


"""
Runs a single simulation for Replication Code given the parameters. The cache must see
the randomly chosen block to succeed. If there are multiple blocks which it can access,
it totals up the entire speed to make it even faster.

Parameters:
	num_blocks: size of data
	connection_limit: number of connections
	num_codes: irrelevant to this simulation

Returns:
	total_speed: float of the speed, if there are two connections with desired block,
				 the cache will download from both of them, which means their speed is
				 added together
	error: boolean of wheter it is an error.
"""
def cache_single_replication(num_blocks, connection_limit, num_codes=0):
	which_block = random_int(num_blocks)
	succ_conn = 0
	total_speed = 0
	error = True

	for j in range(0,connection_limit):
		block_num = random_int(num_blocks)
		bandwith = random_bandwith()
		if which_block == block_num:
			error = False
			total_speed += bandwith
			succ_conn += 1

	if error:
		return None, error
	else:
		return total_speed, error

from random import *

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
def single_replication(num_blocks,connection_limit,num_codes=0):
	speed = None
	conn_speeds = []
	for j in range(0,connection_limit):
		block_num = int(random()*num_blocks)
		bandwith = random() + 0.5
		conn_speeds.append((block_num,bandwith))

	speeds = [None for _ in range(0, num_blocks)]

	for j in range(0,connection_limit):
		this_block = conn_speeds[j][0]
		this_speed = conn_speeds[j][1]
		if(speeds[this_block] is None) or this_speed > speeds[this_block]:
			speeds[this_block] = this_speed

	error = False
	for item in speeds:
		if item is None:
			error = True
			break;

	if error:
		return None,error
	else:
		speed = min(speeds)
		return speed,error
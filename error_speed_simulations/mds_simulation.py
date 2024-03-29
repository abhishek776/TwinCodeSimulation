from random import *
from heapq import nlargest

"""
Runs a single simulation for MDS Code given the parameters. MDS code functionally
has a user defined number of codes and that the user only needs to access 4 unique
codes to access the data.

Parameters:
	num_blocks: size of data
	connection_limit: number of connections
	num_codes: number of codes inputted by user

Returns:
	speed: float of the speed
	error: boolean of wheter it is an error.
"""
def single_mds(num_blocks,connection_limit,num_codes):
	speed = None
	conn_speeds = []

	for j in range(0,connection_limit):
		code_num = int(random()*num_codes)
		bandwith = random() + 0.5
		conn_speeds.append((code_num,bandwith))

	speeds = {}

	for j in range(0,connection_limit):

		this_code = conn_speeds[j][0]
		this_speed = conn_speeds[j][1]

		if this_code in speeds:
			speeds[this_code] = max(speeds[this_code], this_speed)
		else:
			speeds[this_code] = this_speed

	error = False
	if len(speeds) < num_blocks:
		error = True
		return None, error
	else:
		speed = speeds[nlargest(num_blocks,speeds.keys(),key=lambda i:speeds[i])[num_blocks-1]]
		return speed, error

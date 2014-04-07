from random import *
from heapq import nlargest
from general_functions import *

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
def user_single_mds(num_blocks,connection_limit,num_codes):
	speed = None
	conn_speeds = []

	for j in range(0,connection_limit):
		code_num = random_int(num_codes)
		bandwith = random_bandwith()
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

"""
Runs a single simulation for MDS Code given the parameters for the cache. MDS code functionally
has a user defined number of codes and that the cache can either find the chosen code in its pure
form or it can reconstruct the entire data. It picks whatever has the higher speed.

Parameters:
	num_blocks: size of data
	connection_limit: number of connections
	num_codes: number of codes inputted by user

Returns:
	speed: float of the speed
	error: boolean of wheter it is an error.
"""
def cache_single_mds(num_blocks,connection_limit,num_codes):
	which_code = random_int(num_codes)
	conn_speeds = []

	for j in range(0,connection_limit):
		code_num = random_int(num_codes)
		bandwith = random_bandwith()
		conn_speeds.append((code_num,bandwith))

	reconstruction_speed = 0
	reconstruction_error = True
	chosen_speed = 0
	chosen_error = True
	speeds = {}

	for j in range(0,connection_limit):
		this_code = conn_speeds[j][0]
		this_speed = conn_speeds[j][1]

		if this_code == which_code:
			chosen_speed += this_speed
			chosen_error = False

		if this_code in speeds:
			speeds[this_code] = speeds[this_code] + this_speed
		else:
			speeds[this_code] = this_speed

	if len(speeds) >= num_blocks:
		reconstruction_error = False
		reconstruction_speed = speeds[nlargest(num_blocks,speeds.keys(),key=lambda i:speeds[i])[num_blocks-1]]

	if chosen_error and reconstruction_error:
		return None,True
	elif chosen_error:
		return reconstruction_speed,False
	elif reconstruction_error:
		return chosen_speed,False
	else:
		return max(chosen_speed,reconstruction_speed),False





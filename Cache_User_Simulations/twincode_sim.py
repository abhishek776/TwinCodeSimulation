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
	speed=None
	blue_connections=[]
	red_connections=[]
	which_code = (random_int(2)==0,random_int(num_codes))

	for j in range(0,connection_limit):
		is_red = (random_int(2) == 0)
		code = random_int(num_codes)
		bandwith = random_bandwith()
		if is_red:
			red_connections.append((code,bandwith))
		else:
			blue_connections.append((code,bandwith))


	copy_error = True
	copy_speed = 0

	blue_speeds = {}
	blue_error = True
	blue_speed = None

	for j in range(0,len(blue_connections)):
		this_code = blue_connections[j][0]
		this_speed = blue_connections[j][1]

		if which_code[0] == False and which_code[1] == this_code:
			copy_speed += this_speed
			copy_error = False

		if this_code not in blue_speeds or blue_speeds[this_code] < this_speed:
			blue_speeds[this_code] = this_speed

	if(num_blocks <= len(blue_speeds)):
		blue_error = False
		blue_speed = blue_speeds[nlargest(num_blocks,blue_speeds.keys(),key=lambda i:blue_speeds[i])[num_blocks-1]]



	red_speeds = {}
	red_error = True
	red_speed = None

	for j in range(0,len(red_connections)):
		this_code = red_connections[j][0]
		this_speed = red_connections[j][1]

		if which_code[0] == True and which_code[1] == this_code:
			copy_speed += this_speed
			copy_error = False

		if this_code not in red_speeds or red_speeds[this_code] < this_speed:
			red_speeds[this_code] = this_speed

	if(num_blocks <= len(red_speeds)):
		red_error = False
		red_speed = red_speeds[nlargest(num_blocks,red_speeds.keys(),key=lambda i:red_speeds[i])[num_blocks-1]]



	reconstruct_error = True
	reconstruct_speed = None
	twin_error = True
	twin_speed = None

	if which_code[0] == True:
		if(not red_error):
			reconstruct_error = False
			reconstruct_speed = red_speed
		if(not blue_error):
			twin_error = False
			twin_speed = blue_speed*num_blocks
	else:
		if(not blue_error):
			reconstruct_error = False
			reconstruct_speed = blue_speed
		if(not red_error):
			twin_error = False
			twin_speed = red_speed*num_blocks

	if reconstruct_error and twin_error and copy_error:
		return None,True
	elif not twin_error and not copy_error:
		return max(twin_speed,copy_speed),False
	elif not twin_error and not reconstruct_error:
		return max(twin_speed,reconstruct_speed),False
	elif not copy_error and not reconstruct_error:
		return max(copy_speed,reconstruct_speed),False
	elif not twin_error:
		return twin_speed,False
	elif not copy_error:
		return copy_speed,False
	else:
		return reconstruct_speed,False


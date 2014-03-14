from random import *
from heapq import nlargest

"""
Runs a single simulation for Twin Code given the parameters. The user picks either
a set of Red nodes or Blue nodes. There must be num_blocks number of Red Nodes or
Blue Nodes to be valid.

Parameters:
	num_blocks: size of data
	connection_limit: number of connections
	num_codes: irrelevant to this simulation

Returns:
	speed: float of the speed
	error: boolean of wheter it is an error.
"""
def single_twincode(num_blocks,connection_limit,num_codes=0):
	speed = None
	red_speeds = []
	blue_speeds = []

	for j in range(0,connection_limit):
		bandwith = random() + 0.5
		is_red = int(random()*2) == 0
		if is_red:
			red_speeds.append(bandwith)
		else:
			blue_speeds.append(bandwith)
	
	red_speed = None
	blue_speed = None

	if(len(red_speeds) >= num_blocks):
		red_speed = red_speeds[nlargest(num_blocks,range(len(red_speeds)),key=lambda i:red_speeds[i])[num_blocks-1]]
	if(len(blue_speeds) >= num_blocks):
		blue_speed = blue_speeds[nlargest(num_blocks,range(len(blue_speeds)),key=lambda i:blue_speeds[i])[num_blocks-1]] 

	error = False

	if not red_speed and not blue_speed:
		error = True
		return None,error

	else:
		if red_speed and blue_speed:
			speed = min(red_speed, blue_speed)
		elif red_speed and not blue_speed:
			speed = red_speed
		else:
			speed = blue_speed
		return speed,error


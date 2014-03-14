from random import *
from heapq import nlargest

"""
Runs a single simulation for Fountain Code given the parameters. Fountain code functionally
assumes that each code is unique (n --> inf.) and that the user only needs to access 4 unique
nodes to access the data, which means 0 error rate.

Parameters:
	num_blocks: size of data
	connection_limit: number of connections
	num_codes: irrelevant to this simulation

Returns:
	speed: float of the speed
	error: boolean of wheter it is an error.
"""
def single_fountain(num_blocks,connection_limit,num_codes=0):
	speeds = []
	speed = None
	for j in range(0,connection_limit):
		bandwith = random() + 0.5
		speeds.append(bandwith)

	error = False
	if(len(speeds) < num_blocks):
		error = True
		return None, error
	else:
		speed = speeds[nlargest(num_blocks,range(len(speeds)),key=lambda i:speeds[i])[num_blocks-1]]
		return speed, error

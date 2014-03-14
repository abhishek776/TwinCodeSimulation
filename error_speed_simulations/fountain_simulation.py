from random import *
from heapq import nlargest

def single_fountain(num_blocks,connection_limit,num_codes):
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

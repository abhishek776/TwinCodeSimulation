from random import *
from heapq import nlargest
from general_functions import *
from mds_sim import *

"""
Runs a single simulation for MSR Code given the parameters. MSR code functionally
has a user defined number of codes and that the user only needs to access unique
codes to access the data.

Parameters:
	num_blocks: size of data
	connection_limit:

	 number of connections
	num_codes: number of codes inputted by user (the 'd' value)

Returns:
	speed: float of the speed
	error: boolean of wheter it is an error.
"""
def user_single_msr(num_blocks,connection_limit,num_codes):
	return user_single_mds(num_blocks, connection_limit, num_codes)


"""
Runs a single simulation for MSR Code given the parameters for the cache. MSR code functionally
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
def cache_single_msr(num_blocks,connection_limit,num_codes):
	which_code = random_int(num_codes)
	multiple = num_codes / num_blocks

	conn_speeds = []
	for j in range(0,connection_limit):
		code_num = random_int(num_codes)
		bandwith = random_bandwith()
		conn_speeds.append((code_num,bandwith))

	reconstruction_speed = 0
	reconstruction_error = True
	chosen_speed = 0
	chosen_error = True
	special_speed = 0
	special_error = True

	special_speeds = {}
	recon_speeds = {}

	for j in range(0,connection_limit):
		this_code = conn_speeds[j][0]
		this_speed = conn_speeds[j][1]

		if this_code == which_code:
			chosen_speed += this_speed
			chosen_error = False

		if this_code not in recon_speeds or recon_speeds[this_code] < this_speed:
			recon_speeds[this_code] = this_speed

		if this_code not in special_speeds or special_speeds[this_code] < this_speed:
			special_speeds[this_code] = this_speed

	if len(recon_speeds) >= num_blocks:
		reconstruction_error = False
		reconstruction_speed = recon_speeds[nlargest(num_blocks,recon_speeds.keys(),key=lambda i:recon_speeds[i])[num_blocks-1]]

	if len(special_speeds) >= num_codes:
		special_error = False
		special_speed = special_speeds[nlargest(num_codes, special_speeds.keys(), key=lambda i:special_speeds[i])[num_blocks-1]]
		special_speed = special_speed * ( (multiple-1)*num_blocks + 1)

	if chosen_error and reconstruction_error and special_error:
		return None,True
	elif chosen_error:
		return max(reconstruction_speed, special_speed),False
	elif reconstruction_error:
		return max(chosen_speed,special_speed),False
	elif special_error:
		return max(chosen_speed,reconstruction_speed), False
	elif chosen_error and special_error:
		return reconstruction_speed, False
	elif reconstruction_error and special_error:
		return chosen_speed, False
	elif chosen_error and reconstruction_error:
		return special_speed, False
	else:
		return max(chosen_speed,reconstruction_speed,special_speed),False



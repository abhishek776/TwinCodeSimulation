from fountain_sim import *
from replication_sim import *
from mds_sim import *
from twincode_sim import *

USER_TYPES = {"Replication":user_single_replication,
		 "MDS":user_single_mds,
		 "Fountain":user_single_fountain,
		 "TwinCode":user_single_twin,
		 "All":None
		 }

CACHE_TYPES = {"Replication":cache_single_replication,
		 "MDS":cache_single_mds,
		 "Fountain":cache_single_fountain,
		 "TwinCode":cache_single_twin,
		 "All":None
		 }

"""
A method that has the ability to run any of the four simulations that we created.
Each individual file for each simulation has a method that runs a single simulation
withing the give parameters. This method will deal with all the calculations, number
of simulations, printing messages, and taking inputs. It returns a simulator method
based on the simulation type that was entered into the method.
"""
def create_simulation(cache_or_user, num_blocks, typ, printTrigger=False, takeInputs=False):

	if cache_or_user is "User":
		single_simulation = USER_TYPES[typ]
	elif cache_or_user is "Cache":
		single_simulation = CACHE_TYPES[typ]

	num_codes=num_blocks*2

	if(single_simulation in (user_single_mds,cache_single_mds,user_single_twin,cache_single_twin) and takeInputs):
		inp = str(input("How many codes does your trial have (leave blank for default value)? "))
		if len(inp) > 0:
			num_codes = int(inp)


	def simulator(num_of_simulations,connection_limit=num_blocks*2):

		non_error = 0.0
		total_time = 0.0
		total_speed = 0.0
		num_errors = 0.0

		for i in range(0,num_of_simulations):

			speed, error = single_simulation(num_blocks,connection_limit,num_codes)

			if error:
				num_errors += 1
				if printTrigger:
					print("Simulation " + str(i) + ": ERROR")
			else:
				time = 1.0/speed
				total_time += time
				total_speed += speed
				non_error += 1
				if printTrigger:
					print("Simulation " + str(i) + ": " + str(time) + " seconds")

		error_rate = float(num_errors) / float(num_of_simulations) * 100
		if(non_error > 0):
			average_time = total_time / float(non_error)
			average_speed = total_speed / float(non_error)
		else:
			average_speed = None
			average_time = None

		return error_rate, average_time, average_speed

	return simulator
from random import *
from heapq import nlargest

"""
Returns a simulator method for MDS that works for a specific data size and the specific number
of codes for the MDS determined by the user. The returned method will take in the number of simulations,
how many connections each, and how many codes there are. The default number of connections is twice as 
big as the data size, and default number of blocks is twice as big as the data_size. In order for trial
to be a success, it must only see "num_blocks" unique codes to decode data.
"""
def mds_simulation(num_blocks):

	def simulator(num_of_simulations, number_codes=num_blocks*2, connection_limit=num_blocks*2):

		non_error = 0.0
		total_time = 0.0
		total_speed = 0.0
		num_errors = 0.0
		for i in range(0,num_of_simulations):
			speed = None
			conn_speeds = []

			for j in range(0,connection_limit):
				code_num = int(random()*number_codes + 1)
				bandwith = random() + 0.5
				conn_speeds.append((code_num,bandwith))

			speeds = {}

			for j in range(0,connection_limit):

				this_code = conn_speeds[j][0]
				this_speed = conn_speeds[j][1]

				if this_code in speeds:
					speeds[this_code] = min(speeds[this_code], this_speed)
				else:
					speeds[this_code] = this_speed

			error = False
			if len(speeds) < num_blocks:
				error = True
				print("Simulation " + str(i) + ": ERROR")
				num_errors = num_errors + 1
			else:
				speed = speeds[nlargest(num_blocks,speeds.keys(),key=lambda i:speeds[i])[num_blocks-1]]

			if not error:
				time = 1.0/speed
				total_speed = total_speed + speed
				total_time = total_time + time
				non_error = non_error + 1
				print("Simulation " + str(i) + ": " + str(time) + " seconds")

		error_rate = float(num_errors) / float(num_of_simulations) * 100
		average_time = total_time / float(non_error)
		average_speed = total_speed / float(non_error)

		print("ERROR RATE: " + str(error_rate) + " %")
		print("AVERAGE TIME: " + str(average_time) + " seconds")
		print("AVERAGE SPEED: " + str(average_speed))

	return simulator

"""
Test with the simulation specified in our discussion
"""
def test():
	simulator = mds_simulation(4)
	simulator(100000)


"""
Run simulations based on user inputs. Please follow the parameters defined in the
print statements. I will implement the assertions and exceptions later in the weekend.
"""
def custom_run():
	data_size = input("What is the size of the data: ")
	number_codes = input("How many codes does your MDS have: ")
	simulator = mds_simulation(int(data_size))
	simulations = input("How many simulations: ")
	connections = input("How many connections: ")
	simulator(int(simulations),int(number_codes),int(connections))
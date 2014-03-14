from Node import *
from ReplicationNode import *
from Decoding import *
from random import *


"""
Returns a simulator method for replication that works for a specific data size. The
returned method will take in the number of simulations and how many connections each
"user" can make. The default number of connections is twice as big as the data size.
"""
def replication_simulation(num_blocks):

	def simulator(num_of_simulations, connection_limit=num_blocks*2):

		non_error = 0.0
		total_time = 0.0
		num_errors = 0.0
		for i in range(0,num_of_simulations):
			speed = None
			connections = []
			bandwiths = []
			for j in range(0,connection_limit):
				block_num = int(random()*num_blocks + 1)
				bandwith = random() + 0.5
				node = ReplicationNode(j,1,num_blocks,[block_num])
				connections.append(node)
				bandwiths.append(bandwith)

			speeds = [None for _ in range(0, num_blocks)]

			for j in range(0,connection_limit):
				this_connection = connections[j]
				this_speed = bandwiths[j]
				which_block = this_connection.get_contents()[0]
				if(speeds[which_block-1] is None) or this_speed > speeds[which_block-1]:
					speeds[which_block-1] = this_speed

			error = False
			for item in speeds:
				if item is None:
					num_errors = num_errors + 1
					print("Simulation " + str(i) + ": ERROR")
					error = True
					break;

			if not error:
				speed = min(speeds)
				time = 1.0/speed
				total_time = total_time + time
				non_error = non_error + 1
				print("Simulation " + str(i) + ": " + str(time) + " seconds")

		error_rate = float(num_errors) / float(num_of_simulations) * 100
		average_time = total_time / float(non_error)

		print("ERROR RATE: " + str(error_rate) + " %")
		print("AVERAGE TIME: " + str(average_time) + " seconds")

	return simulator

"""
Test with the simulation specified in our discussion
"""
def test():
	simulator = replication_simulation(4)
	simulator(1000000)


"""
Run simulations based on user inputs. Please follow the parameters defined in the
print statements. I will implement the assertions and exceptions later in the weekend.
"""
def custom_run():
	data_size = input("What is the size of the data (please enter a perfect square): ")
	simulator = replication_simulation(int(data_size))
	simulations = input("How many simulations (please enter positive integer): ")
	connections = input("How many connections (please enter positive integer): ")
	simulator(int(simulations),int(connections))


"""
Run a million simulations
"""
test()

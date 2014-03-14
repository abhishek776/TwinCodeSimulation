from random import *
from heapq import nlargest

def fountain_simulation(num_blocks):

	def simulator(num_of_simulations, connection_limit=num_blocks*2):

		non_error = 0.0
		total_time = 0.0
		total_speed = 0.0
		num_errors = 0.0
		for i in range(0,num_of_simulations):			
			speeds = []
			speed = None
			for j in range(0,connection_limit):
				bandwith = random() + 0.5
				speeds.append(bandwith)

			error = False
			if(len(speeds) < num_blocks):
				error = True
				print("Simulation " + str(i) + ": ERROR")
				num_errors = num_errors + 1
			else:
				speed = speeds[nlargest(num_blocks,range(len(speeds)),key=lambda i:speeds[i])[num_blocks-1]]


			if not error:
				time = 1.0/speed
				total_time = total_time + time
				total_speed = total_speed + speed
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
	simulator = fountain_simulation(4)
	simulator(100000)


"""
Run simulations based on user inputs. Please follow the parameters defined in the
print statements. I will implement the assertions and exceptions later in the weekend.
"""
def custom_run():
	data_size = input("What is the size of the data: ")
	simulator = fountain_simulation(int(data_size))
	simulations = input("How many simulations: ")
	connections = input("How many connections: ")
	simulator(int(simulations),int(connections))
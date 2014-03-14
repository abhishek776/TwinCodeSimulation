from random import *
from heapq import nlargest

def twincode_simulation(num_blocks,printTrigger=False):

	def simulator(num_of_simulations, connection_limit=num_blocks*2):

		non_error = 0.0
		total_time = 0.0
		total_speed = 0.0
		num_errors = 0.0
		for i in range(0,num_of_simulations):
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
			error = False


			if(len(red_speeds) >= num_blocks):
				red_speed = red_speeds[nlargest(num_blocks,range(len(red_speeds)),key=lambda i:red_speeds[i])[num_blocks-1]]
			if(len(blue_speeds) >= num_blocks):
				blue_speed = blue_speeds[nlargest(num_blocks,range(len(blue_speeds)),key=lambda i:blue_speeds[i])[num_blocks-1]] 

			if not red_speed and not blue_speed:
				error = True
				print("Simulation " + str(i) + ": ERROR")
				num_errors = num_errors + 1
			elif red_speed and blue_speed:
				speed = min(red_speed, blue_speed)
			elif red_speed and not blue_speed:
				speed = red_speed
			else:
				speed = blue_speed

			if not error:
				time = 1.0/speed
				total_time = total_time + time
				total_speed = total_speed + speed
				non_error = non_error + 1
				print("Simulation " + str(i) + ": " + str(time) + " seconds")

		error_rate = float(num_errors) / float(num_of_simulations) * 100
		average_time = total_time / float(non_error)
		average_speed = total_speed / float(non_error)

		return error_rate, average_time, average_speed

	return simulator

"""
Test with the simulation specified in our discussion
"""
def test():
	simulator = twincode_simulation(4,True)
	results = simulator(100000)
	print("ERROR RATE: " + str(results[0]) + " %")
	print("AVERAGE TIME: " + str(results[1]) + " seconds")
	print("AVERAGE SPEED: " + str(results[2]))


"""
Run simulations based on user inputs. Please follow the parameters defined in the
print statements. I will implement the assertions and exceptions later in the weekend.
"""
def custom_run():
	data_size = input("What is the size of the data: ")
	simulator = twincode_simulation(int(data_size),True)
	simulations = input("How many simulations: ")
	connections = input("How many connections: ")
	simulator(int(simulations),int(connections))
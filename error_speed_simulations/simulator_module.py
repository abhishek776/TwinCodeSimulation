from replication_simulation import single_replication
from mds_simulation import single_mds
from fountain_simulation import single_fountain
from twincode_simulation import single_twincode

TYPES = {"Replication":single_replication,
		 "MDS":single_mds,
		 "Fountain":single_fountain,
		 "TwinCode":single_twincode,
		 "All":None
		 }

"""
A method that has the ability to run any of the four simulations that we created.
Each individual file for each simulation has a method that runs a single simulation
withing the give parameters. This method will deal with all the calculations, number
of simulations, printing messages, and taking inputs. It returns a simulator method
based on the simulation type that was entered into the method.
"""
def create_simulation(num_blocks, typ, printTrigger=False, takeInputs=False):

	single_simulation = TYPES[typ]
	num_codes=num_blocks*2

	if((single_simulation == single_mds or single_simulation == single_twincode) and takeInputs):
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
		average_time = total_time / float(non_error)
		average_speed = total_speed / float(non_error)

		return error_rate, average_time, average_speed

	return simulator

"""
Method that prints our results.
"""
def print_results(num_simulations,results):
	print  #Empty Line
	print("NUMBER OF SIMULATIONS: " + str(num_simulations))
	print("ERROR RATE: " + str(results[0]) + " %")
	print("AVERAGE TIME: " + str(results[1]) + " seconds")
	print("AVERAGE SPEED: " + str(results[2]))
	print  # Empty Line


"""
Runs the default replication test. Size 4, 8 Connections.
"""
def replication_test(num_simulations=100000, printTrigger=True):
	simulator = create_simulation(4,"Replication",printTrigger)
	results = simulator(num_simulations)
	print_results(num_simulations, results)

"""
Runs the default MDS test. Size 4, 8 Connections, 8 Codes.
"""
def mds_test(num_simulations=100000, printTrigger=True,takeInputs=False):
	simulator = create_simulation(4,"MDS",printTrigger,takeInputs)
	results = simulator(num_simulations)
	print_results(num_simulations, results)

"""
Runs the default Fountain test. Size 4, 8 Connections. codes -> infinity.
"""
def fountain_test(num_simulations=100000, printTrigger=True):
	simulator = create_simulation(4,"Fountain",printTrigger)
	results = simulator(num_simulations)
	print_results(num_simulations, results)

"""
Runs the default Twin Code test. Size 4, 8 Connections. codes -> infinity.
"""
def twin_test(num_simulations=100000, printTrigger=True):
	simulator = create_simulation(4,"TwinCode",printTrigger)
	results = simulator(num_simulations)
	print_results(num_simulations, results)

"""
Tests all of them with default values.
"""
def test_all(num_simulations=100000, printTrigger=False):
	print("\n---- Replication Test ----")
	replication_test(num_simulations, printTrigger)
	print("\n---- MDS Test ----")
	mds_test(num_simulations, printTrigger)
	print("\n---- Fountain Test ----")
	fountain_test(num_simulations, printTrigger)
	print("\n---- TwinCode Test ----")
	twin_test(num_simulations, printTrigger)


TEST_TYPES = {"Replication":replication_test,
		 "MDS":mds_test,
		 "Fountain":fountain_test,
		 "TwinCode":twin_test,
		 "All":test_all
		 }
"""
You can choose with default simulation you want to run and number of simulations
"""
def test():
	isValid = False
	inp = None
	while not isValid:
		inp = raw_input("Replication or MDS or Fountain or TwinCode or All? ")
		if inp in TEST_TYPES.keys():
			isValid = True

	sims = raw_input("Number of Simulations (enter integer or leave blank for default? ")
	print # Empty Line
	if(len(sims) == 0):
		TEST_TYPES[inp]()
	else:
		TEST_TYPES[inp](int(sims))

"""
Completely custom simulation run.
"""
def custom_run():
	data = int(input("What is the size of your data? "))
	connections = int(input("How many connections does the user have? "))
	num_sims = int(input("How many simulations would you like? "))
	typ = None
	isValid = False
	while not isValid:
		inp = raw_input("Replication or MDS or Fountain or TwinCode or All? ")
		if inp in TYPES.keys():
			typ = inp
			isValid = True

	if TYPES[typ] is None: # All simulations
		print("\n---- Replication Test ----")
		results = create_simulation(data, "Replication", False, True)(num_sims, connections)
		print_results(num_sims,results)

		print("\n---- MDS Test ----")
		results = create_simulation(data, "MDS", False, True)(num_sims, connections)
		print_results(num_sims,results)

		print("\n---- Fountain Test ----")
		results = create_simulation(data, "Fountain", False, True)(num_sims, connections)
		print_results(num_sims,results)

		print("\n---- TwinCode Test ----")
		results = create_simulation(data, "TwinCode", False, True)(num_sims, connections)
		print_results(num_sims,results)

	else:
		results = create_simulation(data, typ, True, True)(num_sims, connections)
		print_results(num_sims,results)








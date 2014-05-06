from simulator_module import *

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


def generic_test(typ,num_blocks=4,num_codes=8,num_simulations=10000, printTrigger=False):
	print # Empty Line
	print "--------------- " + typ.upper() + " RESULTS ---------------"
	print # Empty Line
	print "\t-------- USER RESULTS--------"
	simulator = create_simulation("User",num_blocks,typ,printTrigger)
	results = simulator(num_simulations,num_codes)
	print_results(num_simulations,results)

	print # Empty Line
	print "\t-------- CACHE RESULTS--------"
	simulator = create_simulation("Cache",num_blocks,typ,printTrigger)
	results = simulator(num_simulations,num_codes)
	print_results(num_simulations, results)	


"""
Runs the default replication test. Size 4, 8 Connections.
"""
def replication_test(num_blocks=4,num_codes=8,num_simulations=10000, printTrigger=True):
	generic_test("Replication", num_blocks, num_codes,num_simulations, printTrigger)


"""
Runs the default MDS test. Size 4, 8 Connections, 8 Codes.
"""
def mds_test(num_blocks=4,num_codes=8,num_simulations=10000, printTrigger=True):
	generic_test("MDS", num_blocks, num_codes,num_simulations, printTrigger)


"""
Runs the default Fountain test. Size 4, 8 Connections. codes -> infinity.
"""
def fountain_test(num_blocks=4,num_codes=8,num_simulations=10000, printTrigger=True):
	generic_test("Fountain", num_blocks, num_codes,num_simulations, printTrigger)

"""
Runs the default Twin Code test. Size 4, 8 Connections. codes -> infinity.
"""
def twin_test(num_blocks=4,num_codes=8,num_simulations=100000, printTrigger=True):
	generic_test("TwinCode", num_blocks, num_codes,num_simulations, printTrigger)

"""
Runs tests for the MSR Code
"""
def msr_test(num_blocks, num_codes, num_conn, multiple,num_simulations=100000, printTrigger=True):
	generic_test("MSR",num_blocks,num_codes,num_simulations,printTrigger)


def test_variable_connection_generic(typ, num_simulations=10000, num_blocks=4, num_codes=8,printTrigger=True):
	print # Empty Line
	print "---------- " + typ.upper() + " RESULTS ----------"
	user_simulator = create_simulation("User", num_blocks, typ, printTrigger)
	cache_simulator = create_simulation("Cache", num_blocks, typ, printTrigger)
	test_variable_connection_helper(user_simulator, cache_simulator, num_blocks, num_codes,num_simulations)

def test_variable_connection_replication(num_simulations=10000, num_blocks=4, num_codes=8,printTrigger=False):
	test_variable_connection_generic("Replication", num_simulations, num_blocks, num_codes, printTrigger)

def test_variable_connection_mds(num_simulations=10000, num_blocks=4, num_codes=8,printTrigger=False):
	test_variable_connection_generic("MDS", num_simulations, num_blocks, num_codes, printTrigger)

def test_variable_connection_fountain(num_simulations=10000, num_blocks=4, num_codes=8,printTrigger=False):
	test_variable_connection_generic("Fountain", num_simulations, num_blocks, num_codes, printTrigger)

def test_variable_connection_twin(num_simulations=10000, num_blocks=4, num_codes=8,printTrigger=False):
	test_variable_connection_generic("TwinCode", num_simulations, num_blocks, num_codes, printTrigger)

def test_variable_connection_msr(num_blocks, num_codes, num_simulations=10000, printTrigger=False):
	test_variable_connection_generic("MSR", num_simulations, num_blocks, num_codes, printTrigger)

def test_variable_connection_helper(user_simulator, cache_simulator, num_blocks, num_codes,num_simulations):
	print("\n\t-------- n CONNECTIONS-------")
	results = user_simulator(num_simulations, num_codes, num_blocks)
	print # Empty Line
	print "\t\t-------- USER RESULTS--------"
	print_results(num_simulations, results)
	results = cache_simulator(num_simulations, num_codes, num_blocks)
	print # Empty Line
	print "\t\t-------- CACHE RESULTS--------"
	print_results(num_simulations, results)
	print("\n\t------- 2n CONNECTIONS-------")
	results = user_simulator(num_simulations, num_codes, num_blocks*2)
	print # Empty Line
	print "\t\t-------- USER RESULTS--------"
	print_results(num_simulations, results)
	results = cache_simulator(num_simulations, num_codes, num_blocks*2)
	print # Empty Line
	print "\t\t-------- CACHE RESULTS--------"
	print_results(num_simulations, results)
	print("\n\t------- 3n CONNECTIONS-------")
	results = user_simulator(num_simulations, num_codes, num_blocks*3)
	print # Empty Line
	print "\t\t-------- USER RESULTS--------"
	print_results(num_simulations, results)
	results = cache_simulator(num_simulations, num_codes, num_blocks*3)
	print # Empty Line
	print "\t\t-------- CACHE RESULTS--------"
	print_results(num_simulations, results)
	print("\n\t------- 4n CONNECTIONS-------")
	results = user_simulator(num_simulations, num_codes, num_blocks*4)
	print # Empty Line
	print "\t\t-------- USER RESULTS--------"
	print_results(num_simulations, results)
	results = cache_simulator(num_simulations, num_codes, num_blocks*4)
	print # Empty Line
	print "\t\t-------- CACHE RESULTS--------"
	print_results(num_simulations, results)
	print("\n\t------- 5n CONNECTIONS-------")
	results = user_simulator(num_simulations, num_codes, num_blocks*5)
	print # Empty Line
	print "\t\t-------- USER RESULTS--------"
	print_results(num_simulations, results)
	results = cache_simulator(num_simulations, num_codes, num_blocks*5)
	print # Empty Line
	print "\t\t-------- CACHE RESULTS--------"
	print_results(num_simulations, results)
	print("\n\t------- 6n CONNECTIONS-------")
	results = user_simulator(num_simulations, num_codes, num_blocks*6)
	print # Empty Line
	print "\t\t-------- USER RESULTS--------"
	print_results(num_simulations, results)
	results = cache_simulator(num_simulations, num_codes, num_blocks*6)
	print # Empty Line
	print "\t\t-------- CACHE RESULTS--------"
	print_results(num_simulations, results)



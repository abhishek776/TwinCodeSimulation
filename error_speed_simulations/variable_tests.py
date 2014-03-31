from replication_simulation import single_replication
from mds_simulation import single_mds
from fountain_simulation import single_fountain
from twincode_simulation import single_twincode
from simulator_module import *

def test_variable_connection_replication(num_simulations=10000, num_blocks=4, printTrigger=False):
	simulator = create_simulation(num_blocks, "Replication", printTrigger)
	print("\n---- Replication Test ----")
	test_variable_connection_helper(simulator, num_blocks, num_simulations)

def test_variable_connection_mds(num_simulations=10000, num_blocks=4, printTrigger=False, takeInputs=False):
	simulator = create_simulation(num_blocks, "MDS", printTrigger, takeInputs)
	print("\n---- MDS Code Test ----")
	test_variable_connection_helper(simulator, num_blocks, num_simulations)

def test_variable_connection_fountain(num_simulations=10000, num_blocks=4, printTrigger=False):
	simulator = create_simulation(num_blocks, "Fountain", printTrigger)
	print("\n---- Fountain Code Test ----")
	test_variable_connection_helper(simulator, num_blocks, num_simulations)

def test_variable_connection_twin(num_simulations=10000, num_blocks=4, printTrigger=False, takeInputs=False):
	simulator = create_simulation(num_blocks, "TwinCode", printTrigger, takeInputs)
	print("\n---- TwinCode Test ----")
	test_variable_connection_helper(simulator, num_blocks, num_simulations)

def test_variable_connection_helper(simulator, num_blocks, num_simulations):
	print("\n---- n Connections ----")
	results = simulator(num_simulations, num_blocks)
	print_results(num_simulations, results)
	print("\n---- 2n Connections ----")
	results = simulator(num_simulations, num_blocks*2)
	print_results(num_simulations, results)
	print("\n---- 3n Connections ----")
	results = simulator(num_simulations, num_blocks*3)
	print_results(num_simulations, results)
	print("\n---- 4n Connections ----")
	results = simulator(num_simulations, num_blocks*4)
	print_results(num_simulations, results)
	print("\n---- 5n Connections ----")
	results = simulator(num_simulations, num_blocks*5)
	print_results(num_simulations, results)
	print("\n---- 6n Connections ----")
	results = simulator(num_simulations, num_blocks*6)
	print_results(num_simulations, results)

def test_variable_connections(num_simulations=10000, num_blocks=4):
	test_variable_connection_replication(num_simulations,num_blocks)
	test_variable_connection_mds(num_simulations,num_blocks)
	test_variable_connection_fountain(num_simulations,num_blocks)
	test_variable_connection_twin(num_simulations,num_blocks)


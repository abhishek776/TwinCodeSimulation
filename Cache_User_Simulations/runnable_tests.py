from tests import *
from simulator_module import *

def basic_tests(num_blocks=4,num_codes=8,num_simulations=10000,printTrigger=False):
	replication_test(num_blocks, num_codes,num_simulations,printTrigger)
	fountain_test(num_blocks, num_codes,num_simulations,printTrigger)
	mds_test(num_blocks, num_codes,num_simulations,printTrigger)
	twin_test(num_blocks,num_codes,num_simulations,printTrigger)

def variable_tests(num_blocks=4,num_codes=8,num_simulations=10000,printTrigger=False):
	test_variable_connection_replication(num_simulations,num_blocks,num_codes,printTrigger)
	test_variable_connection_fountain(num_simulations,num_blocks,num_codes,printTrigger)
	test_variable_connection_mds(num_simulations,num_blocks,num_codes,printTrigger)
	test_variable_connection_twin(num_simulations,num_blocks,num_codes,printTrigger)


def test_variable_codes_mds_user(num_blocks=8,num_connections=24,num_simulations=10000,printTrigger=False):
	simulator = create_simulation("User", num_blocks, "MDS", printTrigger)
	for i in range(1,100):
		results = simulator(num_simulations,num_blocks*i,num_connections)
		print results[0],results[1],results[2]
	simulator = create_simulation("User",num_blocks,"Fountain",printTrigger)
	results = simulator(num_simulations,num_blocks,num_connections)
	print results[0],results[1],results[2]


def test_variable_codes_mds_cache(num_blocks=8,num_connections=24,num_simulations=10000,printTrigger=False):
	simulator = create_simulation("Cache", num_blocks, "MDS", printTrigger)
	for i in range(1,100):
		results = simulator(num_simulations,num_blocks*i,num_connections)
		print results[0],results[1],results[2]
	simulator = create_simulation("Cache",num_blocks,"Fountain",printTrigger)
	results = simulator(num_simulations,num_blocks,num_connections)
	print results[0],results[1],results[2]


def test_variable_codes_twin_user(num_blocks=8,num_connections=24,num_simulations=10000,printTrigger=False):
	simulator = create_simulation("User", num_blocks, "TwinCode", printTrigger)
	for i in range(1,100):
		results = simulator(num_simulations,num_blocks*i,num_connections)
		print results[0],results[1],results[2]
	results = simulator(num_simulations,10000000000,num_connections)
	print results[0],results[1],results[2]


def test_variable_codes_twin_cache(num_blocks=8,num_connections=24,num_simulations=10000,printTrigger=False):
	simulator = create_simulation("Cache", num_blocks, "TwinCode", printTrigger)
	for i in range(1,100):
		results = simulator(num_simulations,num_blocks*i,num_connections)
		print results[0],results[1],results[2]
	results = simulator(num_simulations,10000000000,num_connections)
	print results[0],results[1],results[2]


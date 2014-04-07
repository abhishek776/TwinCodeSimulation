from tests import *

def basic_tests(num_blocks=4,num_simulations=10000,printTrigger=False,takeInputs=False):
	replication_test(num_blocks, num_simulations,printTrigger,takeInputs)
	fountain_test(num_blocks, num_simulations,printTrigger,takeInputs)
	mds_test(num_blocks, num_simulations,printTrigger,takeInputs)
	twin_test(num_blocks,num_simulations,printTrigger,takeInputs)

def variable_tests(num_blocks=4,num_simulations=10000,printTrigger=False,takeInputs=False):
	test_variable_connection_replication(num_simulations,num_blocks,printTrigger,takeInputs)
	test_variable_connection_fountain(num_simulations,num_blocks,printTrigger,takeInputs)
	test_variable_connection_mds(num_simulations,num_blocks,printTrigger,takeInputs)
	test_variable_connection_twin(num_simulations,num_blocks,printTrigger,takeInputs)
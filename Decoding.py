"""
This method determines whether a list of square matrices of the same size can
be decoded according to fountain code.
"""
def is_decodable(list_of_matrices):

	"""
	Checks if all the items have been decoded.
	"""
	def all_true(found):
		for item in found:
			if not item:
				return False
		return True

	if len(list_of_matrices) == 0:
		return False

	size = len(list_of_matrices[0])**2
	element_connections = [[] for x in range(0,size)]
	list_connections = [[] for x in range(0,len(list_of_matrices))]
	found = [False for x in range(0,size)]


	"""
	This part of the code creates lists on the element 
	side and on the list side in order to run the algorithm 
	to test whether it is decodable.
	"""
	index = 0
	while index < len(list_of_matrices):
		matrix = list_of_matrices[index]
		for i in range(0, len(matrix)):
			for j in range(0, len(matrix)):
				checked = matrix[i][j]
				if(checked):
					element_num = i*len(matrix) + j
					list_connections[index].append(element_num)
					element_connections[element_num].append(index)
		index = index + 1;

	"""
	This part of the code uses the list created in the previous section
	to test if this combination of matrices is decodable.
	"""
	while not all_true(found):
		hasChanged = False
		for lis in list_connections:
			if len(lis) == 1:
				element_index = lis[0]
				found[element_index] = True
				to_delete = element_connections[element_index]
				for index in to_delete:
					list_connections[index].remove(element_index)
				hasChanged = True
		if not hasChanged:
			return False
	return True


"""
This tests the is_decodable method.
"""
def test():
	all_passed = True
	matrix1 = [[True,True, True],[True,True, True],[True, True, True]]
	matrix2 = [[True,True, False],[True,True, False],[True, True, False]]
	matrix3 = [[True,True, False],[False,False, False],[False, False, False]]
	matrix4 = [[False,True, False],[False,False, False],[False, False, False]]
	matrix5 = [[False,False, False],[True,True, True],[False, False, False]]
	matrix6 = [[False,False, False],[True,True, False],[False, False, False]]
	matrix7 = [[False,False, False],[True,False, False],[False, False, False]]
	matrix8 = [[False,False, False],[False,False, False],[True, False, False]]
	matrix9 = [[False,False, False],[False,False, False],[False, True, False]]
	matrix10 = [[False,False, False],[False,False, False],[True, True, True]]
	# Should be True.
	first_test = (is_decodable([matrix1, matrix2, matrix3, matrix4, matrix5, matrix6, matrix7, matrix8, matrix9, matrix10]))
	if(not first_test):
		print("First test failed.")
		all_passed = False

	matrix1 = [[True,True, False],[True,True, False],[True, False, False]]
	matrix2 = [[True, True, False],[True, False, False], [True, True, True]]
	matrix3 = [[True,False, False],[True,True, True],[True, True, False]]
	# Should be False.
	second_test = not (is_decodable([matrix1, matrix2, matrix3]))
	if(not second_test):
		print("Second test failed.")
		all_passed = False


	matrix1 = [[True, True], [True, True]]
	matrix2 = [[False, False], [True, False]]
	matrix3 = [[True, True], [False, False]]
	matrix4 = [[False, True], [False, False]]
	# Should be True
	third_test = is_decodable([matrix1, matrix2, matrix3, matrix4])
	if(not third_test):
		print("Third test failed.")
		all_passed = False

	matrix1 = [[True, True], [True, True]]
	matrix2 = [[False, False], [True, False]]
	matrix3 = [[True, True], [False, False]]
	# Should be False
	fourth_test = not (is_decodable([matrix1, matrix2, matrix3]))
	if(not third_test):
		print("Fourt test failed.")
		all_passed = False

	# Prints if everything is passed.
	if(all_passed):
		print("All tests passed.")


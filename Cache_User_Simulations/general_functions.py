from random import *

def random_bandwith():
	# interm = int(random() * 10)
	# if random == 0:
	# 	return 0.1
	return random() + 0.5
	# if int(random()*10) == 0:
	# 	return 0.1
	# else:
	# 	return 1
	# return 1

def random_int(total_num):
	return int(random()*total_num)


def random_color():
	interm = int(random() * 4)
	if interm < 2:
		return 0
	else:
		return 1
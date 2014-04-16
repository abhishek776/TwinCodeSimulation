from random import *

def random_bandwith():
	# interm = int(random() * 10)
	# if random == 0:
	# 	return 0.1
	return random() + 0.5

def random_int(total_num):
	return int(random()*total_num)


def random_color():
	interm = int(random() * 4)
	if interm == 0:
		return 0
	else:
		return 1
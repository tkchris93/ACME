import numpy as np

def create_word_list():
	filename = 'data.txt'
	file = open(filename, 'r')
	file = file.read()
	file = file.split('\n')
	file = file[:-1]

	return list(np.random.permutation(file))	

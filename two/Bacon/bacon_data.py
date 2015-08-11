# bacon_data.py
"""Volume II Lab 8: Breadth-First Search (Kevin Bacon). Auxiliary file.
Helper code for the 'BaconSolver' class. Do not modify.
"""

def parse(filename="movieData.txt"):
	"""Generate an adjacency dictionary where each key is
	a movie and each value is a list of actors in the movie.
	"""

	# open the file, read it in, and split the text by '\n'
	movieFile = open(filename, 'r')
	movieFile = movieFile.read()
	movieFile = movieFile.split('\n')
	graph = dict()

	# for each movie in the file,
	for line in movieFile:
		# get movie name and list of actors
		names = line.split('/')
		movie = names[0]
		graph[movie] = []
		# add the actors to the dictionary
		for actor in names[1:]:
			graph[movie].append(actor)
	
	return graph			

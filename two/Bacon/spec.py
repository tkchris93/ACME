# spec.py
"""Volume II Lab 8: Breadth-First Search (Kevin Bacon)
<name>
<class>
<date>
"""


# Problems 1-4: Implement the following class
class Graph(object):
    """A graph object, stored as an adjacency dictionary. Each node in the graph is a key in the dictionary.
    The value of each key is a list of the corresponding node's neighbors.
    """

    def __init__(self, adjacency):
        """Store the adjacency dictionary as a class attribute"""
        self.dictionary = adjacency

    # Problem 1
    def __str__(self):
        """String representation: a sorted view of the adjacency dictionary.
        
        Example:
            >>> test = {'A':['B'], 'B':['A', 'C',], 'C':['B']}
            >>> print(Graph(test))
            A: B
            B: A; C
            C: B
        """
        return ""

    # Problem 2
    def search(self, start):
        """Begin at 'start' and perform a breadth-first search until all
        nodes in the graph have been searched. Return a list of values, in
        the order that they were visited. If 'start' is not in the
        adjacency dictionary, raise a ValueError.

        Inputs:
            start: the node to start the search at.

        Returns:
            the list of visited nodes (in order of visitation)

        Example:
            >>> test = {'A':['B'], 'B':['A', 'C',], 'C':['B']}
            >>> Graph(test).search('B')
            ['B', 'A', 'C']
        """
        pass

    # Problem 4
    def shortest_path(self, start, target):
        """Begin at the node containing 'start' and perform a breadth-first
        search until the node containing 'target' is found. Return a list
        containg the shortest path from 'start' to 'target'. If either of
        the inputs are not in the adjacency graph, raise a ValueError.

        Inputs:
            start: the node to start the search at.
            target: the node to search for.

        Returns:
            A list of nodes along the shortest path from start to target,
                including the endpoints.

        Example:
            >>> test = {'A':['B'], 'B':['A', 'C',], 'C':['B']}
            >>> Graph(test).shortest_path('A', 'C')
            ['A', 'B', 'C']
        """
        pass


# Problem 5: Write the following function
def convert_to_networkx(dictionary):
    """Convert 'dictionary' to a networkX object and return it."""
    pass


# Problems 6-8: Implement the following class
class BaconSolver(object):
    """Class for solving the Kevin Bacon problem."""

    # Problem 6
    def __init__(self, filename="movieData.txt"):
        """Initialize the networkX graph and with data from the specified
        file. Store the graph as a class attribute. Also store the collection
        of actors in the file as an attribute.
        """
        pass

    # Problem 6
    def path_to_bacon(self, start, target="Bacon, Kevin"):
        """Find the shortest path from 'start' to 'target'."""
        pass

    # Problem 7
    def bacon_number(self, start, target="Bacon, Kevin"):
        """Return the Bacon number of 'start'."""
        pass

    # Problem 7
    def average_bacon(self, target="Bacon, Kevin"):
        """Calculate the average Bacon number in the data set.
        Note that actors are not guaranteed to be connected to the target.

        Inputs:
            target (str): the node to search the graph for
        """
        pass

# =========================== END OF FILE =============================== #

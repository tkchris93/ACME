# spec.py
"""Volume II Lab 8: Breadth-First Search (Kevin Bacon)
<name>
<class>
<date>
"""
from collections import deque
import networkx as nx
import bacon_data

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
        output = ""
        my_copy = self.dictionary.copy()
        my_keys = my_copy.keys()
        my_keys.sort()
        for i in my_keys:
            my_values = my_copy[i]
            my_values.sort()
            output += i + ": " + '; '.join(my_values) + '\n'
        
        return output

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
        if start not in self.dictionary:
            raise ValueError("Start node not found")
        
        current = start
        visit_queue = deque()
        visited = list()
        marked = set([current])
        
        visited.append(current)
        while True:
            for neighbor in self.dictionary[current]:
                if (neighbor not in marked) and (neighbor not in visited):
                    # if not already visited and not planning on visiting
                    visit_queue.append(neighbor)
                    marked.add(neighbor)
            
            # check for end condition        
            marked.remove(current)
            if len(marked) == 0:
                break
            
            # switch to next neighbor to be checked
            current = visit_queue.popleft()
            visited.append(current)
            
        return visited

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
        if start not in self.dictionary:
            raise ValueError("Start node not found")
        
        current = start
        order = dict()
        visit_queue = deque()
        visited = list()
        marked = set([current])
        
        visited.append(current)
        while True:
            for neighbor in self.dictionary[current]:
                if (neighbor not in marked) and (neighbor not in visited):
                    order[neighbor] = current
                    visit_queue.append(neighbor)
                    marked.add(neighbor)
                    
            marked.remove(current)
            if len(marked) == 0:
                break
            
            current = visit_queue.popleft() 
            visited.append(current)
            if current == target:
                break
        
        # current is target
        path = []
        while current != start:
            path.append(current)
            current = order[current]
            if current == start:
                path.append(current)
        
        path.reverse()
        return path
        
# Problem 5: Write the following function
def convert_to_networkx(dictionary):
    """Convert 'dictionary' to a networkX object and return it."""
    nx_graph = nx.Graph()
    
    for node in dictionary.keys():
        for i in dictionary[node]:
            nx_graph.add_edge(node,i)
            
    return nx_graph

# Problems 6-8: Implement the following class
class BaconSolver(object):
    """Class for solving the Kevin Bacon problem."""

    # Problem 6
    def __init__(self, filename="movieData.txt"):
        """Initialize the networkX graph and with data from the specified
        file. Store the graph as a class attribute. Also store the collection
        of actors in the file as an attribute.
        """
        self.d = bacon_data.parse(filename)
        self.actors = set()
        for actor_list in self.d.values():
            for star in actor_list:
                self.actors.add(star)
        self.graph = convert_to_networkx(self.d)
        
    # Problem 6
    def path_to_bacon(self, start, target="Bacon, Kevin"):
        if start not in self.actors:
            raise ValueError(str(start) + " not found in list")
        elif target not in self.actors:
            raise ValueError(str(target) + " not found in list")
        
        return nx.shortest_path(self.graph, start, target)

    # Problem 7
    def bacon_number(self, start, target="Bacon, Kevin"):
        if start not in self.actors:
            raise ValueError(str(start) + " not found in list")
        elif target not in self.actors:
            raise ValueError(str(target) + " not found in list")
        
        return len(nx.shortest_path(self.graph,start,target))/2

    # Problem 7
    def average_bacon(self, target="Bacon, Kevin"):
        nopath = 0
        total = 0
        for a in self.actors:
            try:
                total += self.bacon_number(a, target)
            except nx.NetworkXNoPath:
                nopath += 1
        return float(total)/(len(self.actors) - nopath)

# =========================== END OF FILE =============================== #

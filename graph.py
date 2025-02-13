#!/usr/bin/env python3

INF = float("inf")

# Simple Node/Vertex of graph implementation:
# each node is defined by: a unique id (autoincremented),
# and a name; the #Test# parameter serves to set a node with __id = -1
class Node:
    # unique id (1, 2, ...); -1 for undefined/unknown/test-only node
    __id = 0
    def __init__(self, name = "Unknown", Test = False):
        if not Test:
            self.__id = Node.__id
            Node.__id += 1
        else:
            self.__id = -1
        self.name = name
    
    def __repr__(self):
        return str(self.__id) + ":" + self.name
    
    def __str__(self):
        return str(self.__id) + ":" + self.name
    
    @property
    def get_id(self):
        return self.__id

# Simple Edge of graph implementation:
# each edge is defined by: its #origin# node,
# its #destination# node, its #weight# (cost) and
# its #direction# (further explanation @line 54)
class Edge:
    def __init__(self, origin = None, destination = None, weight = INF, direction = 0):
        self.origin = origin
        self.destination = destination
        self.weight = weight
        if direction in [-1, 0, 1]:
            self.direction = direction
        else:
            direction = 0

    def __repr__(self):
        return "Edge"
    
    def __str__(self):
        if self.direction == 0:
            return "Edge between " + str(self.origin) + " and " + str(self.destination)
        elif self.direction == 1:
            return "Edge from " + str(self.origin) + " to " + str(self.destination)
        else:
            return "Edge from " + str(self.destination) + " to " + str(self.origin)

# G = (N, E)             | Simple graph object
# N = (A, B, C, D, ...)  | A = 1:"NodeA", B = 2:"NodeB"
# E = (AB, BC, AC, ...)  | AB = (A, B, weight, 1) -> directed graph from node A to node B
#                        | AB = (A, B, weight, 0) -> not directed graph
#                        | AB = (A, B, weight, -1) directed graph from node B to node A, equivalent to:
#                        | BA = (B, A, weight, 1)
class Graph:
    def __init__(self, name = "Graph", nodes = [], edges = []):
        self.name = name
        self.nodes = nodes
        self.edges = edges
        if nodes != []:    
            self.__root = nodes[0]
        self.__node_number = len(nodes)
        self.__edge_number = len(edges)

    def __repr__(self):
        return "Graph"
    
    def __str__(self):
        return self.name

    @property
    def root(self):
        return self.__root

    @property
    def node_number(self):
        return self.__node_number

    @property
    def edge_number(self):
        return self.__edge_number

    @root.setter
    def set_root(self, node):
        if node in self.nodes:
            self.__root = node
            return True
        else:
            return False

    def adjacency_matrix(self):
        matrix = [[0 for i in range(self.__node_number)] for j in range(self.__node_number)]
        
        for i in range(self.__node_number):
            for j in range(self.__node_number):
                for k in range(self.__edge_number):
                    if self.edges[k].origin == self.nodes[i] and self.edges[k].destination == self.nodes[j]:
                        if self.edges[k].direction == 1:
                            matrix[i][j] = 1
                        elif self.edges[k].direction == 0:
                            matrix[i][j] = 1
                            matrix[j][i] = 1
                        elif self.edges[k].direction == -1:
                            matrix[j][i] = 1

        return matrix

    def weight_matrix(self):
        if not self.is_weighted():
            return None
        matrix = [[INF for i in range(self.__node_number)] for j in range(self.__node_number)]

        for i in range(self.__node_number):
            for j in range(self.__node_number):
                for k in range(self.__edge_number):
                    if self.edges[k].origin == self.nodes[i] and self.edges[k].destination == self.nodes[j]:
                        if self.edges[k].direction == 1:
                            matrix[i][j] = self.edges[k].weight
                        elif self.edges[k].direction == 0:
                            matrix[i][j] = self.edges[k].weight
                            matrix[j][i] = self.edges[k].weight
                        elif self.edges[k].direction == -1:
                            matrix[j][i] = self.edges[k].weight
    
        return matrix
              
    def summarize(self):
        print("Graph name: " + self.name)
        print("Number of nodes: " + str(self.__node_number))
        print("Number of edges: " + str(self.__edge_number))
        print("Current root node: " + str(self.__root))

    # Create undirected weighted (optional) edges between nodes following 
    # the positional order in the #self.nodes# list
    def create_undirected_edges(self, weights = []):
        if len(weights) < self.__node_number - 1:
            weights.extend(0 for _ in range(self.__node_number - 1))

        if self.__node_number > 1 and self.__edge_number == 0:
            for i in range(self.__node_number - 1):
                XY = Edge(self.nodes[i], self.nodes[i+1], weights[i], 0)
                self.edges.append(XY)
            self.__edge_number = self.__node_number - 1
        elif self.__edge_number >= 1:
            print("Edges not empty!")
        else:
            print("Not enough nodes!")

    # Create directed weighted (optional) edges between nodes following
    # the positional order in the #self.nodes# list
    def create_edges(self, weights = [], directions = []):
        if len(weights) < self.__node_number - 1:
            weights.extend(0 for _ in range(self.__node_number - 1))

        if len(directions) < self.__node_number - 1:
            directions.extend(1 for _ in range(self.__node_number - 1))

        if self.__node_number > 1 and self.__edge_number == 0:
            for i in range(self.__node_number - 1):
                XY = Edge(self.nodes[i], self.nodes[i+1], weights[i], directions[i])
                self.edges.append(XY)
            self.__edge_number = self.__node_number - 1
        elif self.__edge_number >= 1:
            print("Edges not empty!")
        else:
            print("Not enough nodes!")

    # Return True if the graph is positive weighted
    # <-> all edges have a weight/cost between 0 and +INF
    def is_weighted(self):
        if self.__edge_number == 0:
            return False
        check = True
        for edge in self.edges:
            if edge.weight == INF or edge.weight <= 0:
                check = False
                break
        return check

# Print a generic matrix (list of lists) in a more readable format
def print_matrix(matrix):
    print('\n'.join([' '.join(['{}'.format(item) for item in row]) for row in matrix]))

# Create a Graph istance given its adjacency matrix (#adj_matrix#) and its weight matrix (#w_matrix#) (optional)
def create_graph(name = "Graph", adj_matrix = [], w_matrix = []):
    n = len(adj_matrix)
    if n == 0 or n != len(adj_matrix[0]):
        print("Adjcency matrix format is not valid!")
        return None
    p = len(w_matrix)
    nodes = []
    edges = []
    for i in range(n):
            V = Node("Node_" + str(i))
            nodes.append(V)
    directed = False
    for i in range(n):
        for j in range(n):
            if adj_matrix[i][j] != adj_matrix[j][i]:
                directed = True
    if p == 0 or p != n:
        if p != 0:
            print("Weight matrix format is not valid, ignoring it...")
        for i in range(n):
            for j in range(n):
                if adj_matrix[i][j] == 1:
                    if not directed:
                        E = Edge(nodes[i], nodes[j], weight = 0, direction = 0)
                        adj_matrix[j][i] = 0
                    else:
                        E = Edge(nodes[i], nodes[j], weight = 0, direction = 1)
                    edges.append(E)
    else:
        for i in range(n):
            for j in range(n):
                if adj_matrix[i][j] == 1:
                    if not directed:
                        E = Edge(nodes[i], nodes[j], weight = w_matrix[i][j], direction = 0)
                        adj_matrix[j][i] = 0
                    else:
                        E = Edge(nodes[i], nodes[j], weight = w_matrix[i][j], direction = 1)
                    edges.append(E)

    return Graph(name, nodes, edges)

# Test __main__
if __name__ == "__main__":
    wiki_adj_matrix = [[0, 1, 0, 0, 1, 0, 0],
                       [1, 0, 1, 1, 0, 0, 0],
                       [0, 1, 0, 0, 0, 0, 1],
                       [0, 1, 0, 0, 1, 1, 0],
                       [1, 0, 0, 1, 0, 1, 0],
                       [0, 0, 0, 1, 1, 0, 1],
                       [0, 0, 1, 0, 0, 1, 0]]
        
    wiki_w_matrix = [[INF, 2, INF, INF, 8, INF, INF],
                    [2, INF, 6, 2, INF, INF, INF],
                    [INF, 6, INF, INF, INF, INF, 5],
                    [INF, 2, INF, INF, 2, 9, INF],
                    [8, INF, INF, 2, INF, 3, INF],
                    [INF, INF, INF, 9, 3, INF, 1],
                    [INF, INF, 5, INF, INF, 1, INF]]

    print_matrix(wiki_adj_matrix)
    print_matrix(wiki_w_matrix)
    G1 = create_graph(name = "WikiGraph1", adj_matrix = wiki_adj_matrix)
    print(G1.is_weighted())
    print(G1)
    G1.summarize()
    print()
    G2 = create_graph(name = "WikiGraph2", adj_matrix = wiki_adj_matrix, w_matrix = wiki_w_matrix)
    print(G2.is_weighted())
    print(G2)
    G2.summarize()
    print_matrix(G1.adjacency_matrix())
    print("Done!")

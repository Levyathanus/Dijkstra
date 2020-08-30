#!/bin/python3

# G = (N, E)             | Simple graph object
# N = (A, B, C, D, ...)  | A = 1:"NodeA", B = 2:"NodeB"
# E = (AB, BC, AC, ...)  | AB = (A, B, weight, 1) -> directed graph from node 1 to node 2
#                        | AB = (A, B, weight, 0) -> not directed graph
#                        | AB = (A, B, weight, -1) directed graph from node 2 to node 1, equivalent to:
#                        | BA = (B, A, weight, 1)

class Node:
    # unique id (1, 2, ...); -1 for undefined/unknown/test-only node
    __id = 0
    def __init__(self, name = "Unknown", Test = False):
        if not Test:
            self.__id = Node.__id + 1
            Node.__id += 1
        else:
            self.__id = -1
        self.name = name
    
    def __repr__(self):
        return "Node/Vertex"
    
    def __str__(self):
        return str(self.__id) + ":" + self.name
    
    @property
    def get_id(self):
        return self.__id

class Edge:
    def __init__(self, origin = None, destination = None, weight = float("inf"), direction = 0):
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

    def weights_matrix(self):
        if not self.is_weighted():
            return None
        matrix = [[0 for i in range(self.__node_number)] for j in range(self.__node_number)]

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

    def is_weighted(self):
        if self.__edge_number == 0:
            return False
        check = True
        for edge in self.edges:
            if edge.weight == float('inf') or edge.weight <= 0:
                check = False
                break
        return check

def print_matrix(matrix):
    print('\n'.join([' '.join(['{}'.format(item) for item in row]) for row in matrix]))

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
    directed = True
    for i in range(n):
        for j in range(n):
            if adj_matrix[i][j] != adj_matrix[j][i]:
                directed = False
    if p == 0 or p != n:
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


if __name__ == "__main__":
    #a = Node("Test", Test = True)
    #b = Node("Node_1_b")
    #c = Node("Node_2_c")
    #print(a)
    #print(b)
    #print(c)

    #nodes = [b, c]
    #G = Graph("TestGraph", nodes)
    #G.create_undirected_edges()
    #G.summarize()
    #print(G.edges[0])
    #print_matrix(G.adjacency_matrix())
    #print(G.is_weighted())
    #P = G.weights_matrix()
    #print(P)
    wiki_adj_matrix = [[0,1,0,0,1,0,0],
                       [1,0,1,1,0,0,0],    
                       [0,1,0,0,0,0,1],
                       [0,1,0,0,1,1,0],
                       [1,0,0,1,0,0,0],
                       [0,0,0,1,1,0,1],
                       [0,0,1,0,0,1,0]]

    print_matrix(wiki_adj_matrix)
    G = create_graph(name = "WikiGraph", adj_matrix = wiki_adj_matrix)
    print(G.is_weighted())
    print(G)
    G.summarize()
    print("Done!")

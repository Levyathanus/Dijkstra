#!/bin/python3

# G = (N, E)         | Simple graph object
# N = (A, B, C, ...) | A = (1, "NodeA"), B = (2, "NodeB")
# E = (AB, BC, ...)  | AB = (1, 2, weight, 1) -> directed graph from node 1 to node 2
#                    | AB = (1, 2, weight, 0) -> not directed graph
#                    | AB = (1, 2, weight, -1) directed graph from node 2 to node 1, equivalent to:
#                    | BA = (2, 1, weight, 1)

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
        self.direction = direction

    def __repr__(self):
        return "Edge"
    
    def __str__(self):
        return "Edge between: " + str(self.origin) + " and " + str(self.destination)

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

    def summarize(self):
        print("Graph name: " + self.name)
        print("Number of nodes: " + str(self.__node_number))
        print("Number of edges: " + str(self.__edge_number))
        print("Current root node: " + str(self.__root))
    
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

    def create_undirected_edges(self, weights = []):
        if len(weights) < self.__node_number -1:
            weights.extend(0 for _ in range(self.__node_number - 1))

        if self.__node_number > 1 and self.__edge_number == 0:
            for i in range(self.__node_number - 1):
                XY = Edge(self.nodes[i], self.nodes[i+1], weights[i], 0)
                self.edges.append(XY)
            self.__edge_number = self.__node_number - 1
        elif self.__node_number > 1:
            print("Edges not empty!")
        else:
            print("Not enough nodes!")

    def create_edges(self, weights = [], directions = []):
        if len(weights) < self.__node_number -1:
            weights.extend(0 for _ in range(self.__node_number - 1))

        if self.__node_number > 1 and self.__edge_number == 0:
            for i in range(self.__node_number - 1):
                XY = Edge(self.nodes[i], self.nodes[i+1], weights[i], directions[i])
                self.edges.append(XY)
            self.__edge_number = self.__node_number - 1
        elif self.__node_number > 1:
            print("Edges not empty!")
        else:
            print("Not enough nodes!")


if __name__ == "__main__":
    a = Node("Test", Test = True)
    b = Node("Node_1_b")
    c = Node("Node_2_c")
    print(a)
    print(b)
    print(c)

    nodes = [b, c]
    G = Graph("TestGraph", nodes)
    G.create_undirected_edges()
    G.summarize()
    print(G.edges[0])
    print("Done!")

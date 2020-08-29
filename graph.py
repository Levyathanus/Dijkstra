#!/bin/python3

# G = (N, E)         | Simple graph object
# N = (A, B, C, ...) | A = (1, "NodeA"), B = (2, "NodeB")
# E = (AB, BC, ...)  | AB = (1, 2, weight, 1) -> directed graph from node 1 to node 2
#                    | AB = (1, 2, weight, 0) -> not directed graph
#                    | AB = (1, 2, weight, -1) directed graph from node 2 to node 1, equivalent to:
#                    | BA = (2, 1, weight, 1)

class Node:
    # unique id (1, 2, ...); 0 for undefined/unknown/test-only node
    def __init__(self, id = 0, name = "Unknown"):
        self.id = id
        self.name = name

class Edge:
    def __init__(self, origin = 0, destination = 0, weight = float("inf"), direction = 0):
        self.origin = origin
        self.destination = destination
        self.weight = weight
        self.direction = direction

class Graph:
    def __init__(self, name = "Graph", nodes = [], edges = []):
        self.name = name
        self.nodes = nodes
        self.edges = edges
        if nodes != []:    
            self.__root = nodes[0]
        self.__node_number = len(nodes)
        self.__edge_number = len(edges)

    @property
    def get_root(self):
        return self.__root

    @property
    def get_node_number(self):
        return self.__node_number

    @property
    def get_edge_number(self):
        return self.__edge_number
    
    @set_root.setter
    def set_root(self, node):
        if node in self.nodes:
            self.__root = node
            return True
        else:
            return False

    def create_undirected_edges(self, weights = []):
        if self.__node_number > 1 and self.__edge_number == 0:
            for i in range(self.__node_number - 1):
                XY = Edge(self.nodes[i], self.nodes[i+1], weights[i], 0)
                self.edges.append(XY)
        elif self.__node_number > 1:
            print("Edges not empty!")
        else:
            print("Not enough nodes!")

    def create_edges(self, weights = [], directions = []):
        if self.__node_number > 1 and self.__edge_number == 0:
            for i in range(self.__node_number - 1):
                XY = Edge(self.nodes[i], self.nodes[i+1], weights[i], directions[i])
                self.edges.append(XY)
        elif self.__node_number > 1:
            print("Edges not empty!")
        else:
            print("Not enough nodes!")


if __name__ == "__main__":
    print("Done!")

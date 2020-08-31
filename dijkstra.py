import graph
INF = float("inf")
# G = (N, E)
# P = Set of permanently labeled nodes (root-node distance is defined)
# d[i][j] = cost/weight of the direct link between i and j nodes (d[i][j] = INF if i and j haven't a direct link) 
# D[j] = total cost/weight of the path from root to the j node


def dijkstra(G, root = None, end = None):
    if not G.is_weighted():
        print("Cannot perform Dijkstra algorithm on a not weighted graph!")
        return None
    if root == None:
        root = G.root
    N = [node for node in G.nodes]
    P = []
    D = [0*len(N)]
    d = G.weight_matrix
    s = 0 # root index
    for j in range(G.node_number):
        if N[j] == root:
            D[j] = 0
            s = j
        else:
            D[j] = INF

    if end is not None:
        while P != N:
            for node in diff(N, P):
                
           


            
def diff(list1, list2):
    return (list(list(set(list1)-set(list2)) + list(set(list2)-set(list1))))


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

    G1 = graph.create_graph(name="WikiGraph1", adj_matrix=wiki_adj_matrix)
    G2 = graph.create_graph(name="WikiGraph2", adj_matrix=wiki_adj_matrix, w_matrix=wiki_w_matrix)
    ACCM = dijkstra(G2)

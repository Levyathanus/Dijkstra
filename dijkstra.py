import graph
INF = float("inf")
# G = (N, E)
# P = Set of permanently labeled nodes (root-node distance is defined)
# d[i][j] = cost/weight of the direct link between i and j nodes (d[i][j] = INF if i and j haven't a direct link) (<-> weight matrix)
# D[j] = total cost/weight of the path from root to the j node


def dijkstra(G, root = None, end = None):
    if not G.is_weighted():
        print("Cannot perform Dijkstra algorithm on a not weighted graph!")
        return None
    if root == None:
        root = G.root
    N = [node for node in G.nodes]
    P = [[] for _ in range(len(G.nodes))]
    D = [0]*len(N)
    DIST = [0]*len(N)
    d = 0

    for j in range(len(N)):
        if N[j] == root:
            D[j] = 0
        else:
            D[j] = INF

    if end is None:
        end = G.nodes[-1]
        while not empty(N):
            #print(N, D)
            d = min(D)
            u = N[D.index(d)]
            x = N.index(u)
            if D[x] == INF:
                break
            V = neighbors(u, G) 
            #print(V, u, d)
            for v in V:
                if v in N:
                    alt = D[x] + dist(u, v, G)
                    #print(D[x], alt)
                    if alt < D[N.index(v)]:
                        D[N.index(v)] = alt
                        if P.count(u) == 0:
                            P[N.index(v)] = u
                        DIST[N.index(v)] = D[x]
            N[x] = []
            D[x] = INF
            #print()
    P, DIST = dual_filter(P, DIST)
    DIST.insert(0, 0)
    P.append(end)
    return P, DIST

def dist(u, v, G):
    for edge in G.edges:
        if edge.origin == u and edge.destination == v:
            return edge.weight
    print("No edge found between " + str(u) + " and " + str(v))
    return 0

def neighbors(u, G):
    V = []
    for edge in G.edges:
        if edge.origin == u and edge.destination != u:
            V.append(edge.destination)
    return V

def empty(N):
    for item in N:
        if item != []:
            return False
    return True
    
def dual_filter(l1, l2):
    if len(l1) == len(l2):
        for i in range(len(l1)):
            if l1[i] == []:
                l2[i] = []
        return list(filter(None, l1)), list(filter(None, l2))
    else:
        return None
    
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

    #G1 = graph.create_graph(name="WikiGraph1", adj_matrix=wiki_adj_matrix)
    G2 = graph.create_graph(name="WikiGraph2", adj_matrix=wiki_adj_matrix, w_matrix=wiki_w_matrix)
    #G2.summarize()
    ACCM, D = dijkstra(G2)
    print(ACCM, D)

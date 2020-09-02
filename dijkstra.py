import graph
INF = float("inf")

# G = (N, E): input graph (refer to graph.py). It must be a weighted graph!
# root: starting node
# end: arrival node
# P: ordered list of connected nodes from root to end minimizing the total path cost (#1 returned value)
# D: distances between the current node and its neighbors (changing labels)
# DIST: definitive labels for each node of the P list (costs) (#2 returned value)
# d: minimum distance from the previous node

def dijkstra(G, root = None, end = None):
    if not G.is_weighted():
        print("Cannot perform Dijkstra algorithm on a not weighted graph!")
        return None
    if root is None:
        root = G.root
    if end is None:
        end = G.nodes[-1]
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
    
    while not empty(N):
        d = min(D)
        u = N[D.index(d)]
        x = N.index(u)
        if u == end:
            end_dist = D[x]
            break
        if D[x] == INF:
            break
        V = neighbors(u, G)
        for v in V:
            if v in N:
                alt = D[x] + dist(u, v, G)
                if alt < D[N.index(v)]:
                    D[N.index(v)] = alt
                    if P.count(u) == 0:
                        P[N.index(v)] = u
                    DIST[N.index(v)] = D[x]
        N[x] = []
        D[x] = INF

    P, DIST = dual_filter(P, DIST)
    DIST.insert(0, 0)
    DIST.append(end_dist)
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
        return l1, l2
    
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


    slide_adj_matrix = [[0, 1, 0, 0, 0, 1],
                        [1, 0, 1, 0, 1, 1],
                        [0, 1, 0, 1, 0, 0],
                        [0, 0, 1, 0, 1, 1],
                        [0, 1, 0, 1, 0, 1],
                        [1, 1, 0, 1, 1, 0]]
    
    slide_w_matrix = [[INF, 1, INF, INF, INF, 3],
                     [1, INF, 3, INF, 5, 1],
                     [INF, 3, INF, 2, INF, INF],
                     [INF, INF, 2, INF, 1, 6],
                     [INF, 5, INF, 1, INF, 2],
                      [3, 1, INF, 6, 2, INF]]
    
    #G = graph.create_graph(name="WikiGraph2", adj_matrix=wiki_adj_matrix, w_matrix=wiki_w_matrix)
    G = graph.create_graph(name="SlideGraph", adj_matrix=slide_adj_matrix, w_matrix=slide_w_matrix)
    G.summarize()
    k = input()
    h = input()
    if k == '':
        if h == '':
           ACCM, D = dijkstra(G)
        else:
            h = int(h)
            ACCM, D = dijkstra(G, None, end=G.nodes[h])
    elif h == '':
        k = int(k)
        ACCM, D = dijkstra(G, root=G.nodes[k])
    else:
        k = int(k)
        h = int(h)
        ACCM, D = dijkstra(G, root=G.nodes[k], end=G.nodes[h])
    
    print(ACCM, D)

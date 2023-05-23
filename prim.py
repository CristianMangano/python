def minpop2(seq):
"""
trova il minimo da tutti gli archi passati come liste di tuple

"""
    wmin, umin, vmin = seq[0]
    for w, u, v in seq:
        if w < wmin:
            wmin, umin, vmin = w, u, v
    return wmin, umin, vmin

def prim_jarnik(graph, start):
    mininum_spanning_tree = dict()
    X = set() # l'insieme di tutti i nodi esaminati
    X.add(start)
    nedge = 0 # chiave dizionario con l'indice degli archi
    while len(X) != len(graph):
        crossing = [] # lista corrente dei nodi presi in esame una e una sola volta
        for x in X:
            for k in graph:
            # k varierà prima
                if k not in X and k in graph[x]:
                    """
                    nota che graph[x][k] è sempre un numero che descrive il peso dell'arco                    
                    """
                    crossing.append((graph[x][k], x, k))
        w, u, v = minpop2(crossing)
        mininum_spanning_tree[nedge] = (w, u, v)
        X.add(v) # da questo nodo vado avanti ad espolare il grafo
        nedge += 1
    return mininum_spanning_tree

grafo = {
    'A': {'B': 2, 'C': 4, 'D': 1},
    'B': {'A': 2, 'D': 3, 'E': 2},
    'C': {'A': 4, 'D': 2, 'F': 4},
    'D': {'A': 1, 'B': 3, 'C': 2, 'E': 3, 'F': 5},
    'E': {'B': 2, 'D': 3, 'G': 2},
    'F': {'C': 4, 'D': 5, 'G': 1},
    'G': {'E': 2, 'F': 1}
}

prim_jarnik(grafo, 'A')

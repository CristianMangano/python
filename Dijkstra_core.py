"""
calcola la distanza tra 'A' e i vertici adiacenti

"""

grafo = {
    'A': {'B': 2, 'C': 4, 'D': 1},
    'B': {'A': 2, 'D': 3, 'E': 2}
}

nodo = 'A'
distanza = 0 # distanza di A da se stesso

for nodo_corrente in grafo[nodo]:
    peso_arco = grafo[nodo][nodo_corrente]
    distanza_totale = distanza + peso_arco

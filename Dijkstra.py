"""
algoritmi di ottimizzazione o algoritmi greedy (minimizzazione)
pesi non negativi

"""

def distanza_minima(grafo, vertice):
    """
    ritorna un dizionario con tutte le distanze minime da vertice. Attenzione: non 
    ritorna il cammino, mi dice soltato la distanza minima che esiste tra vertice e qualsiasi
    altro nodo. Per trovare il cammino minimo devo usare un'altra funzione che si appoggia a questa
    
    """
    
    nodi = grafo.keys()
    dizionario_distanza_min = dict()
    for nodo in nodi:
        if nodo != vertice:
            dizionario_distanza_min[nodo] = [float("inf"), "da visitare"]
    dizionario_distanza_min[vertice] = [0, "in visita"]
    tuple_di_distanza = (0, vertice)
    queue = list()
    queue.append(tuple_di_distanza)
    while queue:
        distanza, nodo = queue[0][0], queue[0][1]
        queue = queue[1:]
        dizionario_distanza_min[nodo][1] = "visitato"
        for nodo_corrente in grafo[nodo]:
            if dizionario_distanza_min[nodo_corrente][1] == "da visitare": # * se non ho ancora visitato il nodo, e sto parlando dei nodi tra parentesi graffe che hanno come chiave 'A'
                peso_arco = grafo[nodo][nodo_corrente] # * estraggo l'informazione del peso dell'arco, dove nodo = 'A' mentre nodo_corrente varia tra {'B', 'C', 'D'}
                distanza_totale = distanza + peso_arco # * calcolo la distanza totale
                if distanza_totale < dizionario_distanza_min[nodo_corrente][0]: # * scelta greedy
                    dizionario_distanza_min[nodo_corrente][0] = distanza_totale
                    queue.append((distanza_totale, nodo_corrente))
    return dizionario_distanza_min

grafo = {
    'A': {'B': 2},
    'B': {'A': 2, 'C': 3},
    'C': {'B': 3}
}

print(distanza_minima(grafo, 'A'))

"""
output: {'B': [2, 'visitato'], 'C': [5, 'visitato'], 'A': [0, 'visitato']}

mi dice che 'A' è a distanza 0 da se stesso; 'C' è a distanza 5 da 'A'; 'B' è a distanza 2 da 'A'

"""

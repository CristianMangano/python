def crea_albero(node = 'G'):
    albero = {node : {'genitore' : None, 'figlio_destro' : None, 'figlio_sinistro' : None}}
    return albero

def aggiungi_nodo(albero, nodo, genitore, verso):
    if nodo not in albero and genitore in albero and not albero[genitore][verso]:
        albero[nodo] = {'genitore' : genitore, 'figlio_destro' : None, 'figlio_sinistro' : None}
        albero[genitore][verso] = nodo

def preorder(albero, radice, visitati = list()):
    if radice:
        visitati.append(radice)
        if albero[radice]['figlio_sinistro']:
            preorder(albero, albero[radice]['figlio_sinistro'], visitati)
        if albero[radice]['figlio_destro']:
            preorder(albero, albero[radice]['figlio_destro'], visitati)
    return visitati

tree = crea_albero()
aggiungi_nodo(tree, 'F', 'G', 'figlio_destro')
aggiungi_nodo(tree, 'E', 'G', 'figlio_sinistro')
print(preorder(tree, 'G'))

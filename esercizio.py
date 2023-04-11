"""
scrivere una funzione che data una stringa come argomento restitutisce
la lettera presente con maggiore frequenza in una stringa
un set contenente le lettere non presenti nella stringa
"""
def fun(stringa):
    dizionario = dict()
    for carattere in stringa:
        if carattere not in dizionario:
            dizionario[carattere] = 1
        else:
            dizionario[carattere] += 1
    frequenza = max(dizionario.values())
    for key in dizionario:
        if dizionario[key] == frequenza:
            carattere = key
    setU = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'z'}
    setdizionario = set(dizionario)
    setDifferenza = setU - setdizionario
    return carattere, setDifferenza

stringa = 'algoritmi'
carattere, setdifferenza = fun(stringa)
print('il carattere piu frequente: {}. Il set di carattere non utilizzati: {}'.format(carattere, setdifferenza))

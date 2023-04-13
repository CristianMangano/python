def divisore(triangolare):
    divisoriLocali = list()
    for i in range(1, triangolare + 1):
        if triangolare % i == 0:
            divisoriLocali.append(i)
    return divisoriLocali

def triangolare(numero):
    return sum([i for i in range(1, numero + 1)])

def fun(delta):
    listaDeiTriangolari = list()
    dizionario = dict()
    numero = 2
    eof = True
    while eof:
        numeroTriangolare = triangolare(numero)
        listaDeiTriangolari.append(numeroTriangolare)
        divisoriTriangolareCorrente = divisore(numeroTriangolare)
        dizionario[numeroTriangolare] = divisoriTriangolareCorrente
        for chiave in dizionario:
            if len(dizionario[chiave]) > delta:
                eof = False
        numero += 1
    return listaDeiTriangolari[len(listaDeiTriangolari) - 1]

numeroTriangolare = fun(5)
print(numeroTriangolare)

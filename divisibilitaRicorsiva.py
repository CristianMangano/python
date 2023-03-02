''' tutti i numeri naturali < 10 multipli di 3 o 5 sono 3, 6, 9, 5; la cui somma è 23 '''

def my_min(alfa, beta):
    if alfa < beta:
        return alfa
    else:
        return beta

def somma_multipli(a, b, k):
    min_val = my_min(a, b)
    if (k >= min_val) and ((k % a == 0) or (k % b == 0)):
        return k + somma_multipli(a, b, (k - 1))
    if (k > min_val):
        return somma_multipli(a, b, (k - 1))
    if k < min_val:
        return 0
    
ris = somma_multipli(3, 5, 999)
print(ris)

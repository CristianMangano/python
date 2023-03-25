"""Scrivi una funzione ricorsiva find_largest_prime_factor(number, largest_prime_factor=1)
che calcoli e ritorni il più grande fattore primo del numero dato.
questo codice restituisce invece il minimo"""

def find_largest_prime_factor(number, largest_prime_factor=1):
    ret = 1
    if number is not largest_prime_factor and number%largest_prime_factor is not 0 or largest_prime_factor is 1:
        return find_largest_prime_factor(number, largest_prime_factor + 1)
    if number is not largest_prime_factor and number%largest_prime_factor is 0 and largest_prime_factor > 1:
        ret = largest_prime_factor
        find_largest_prime_factor(number, largest_prime_factor + 1)
        return ret
    if number is largest_prime_factor:
        return ret

print(find_largest_prime_factor(4))

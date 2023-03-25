"""Scrivi una funzione ricorsiva find_largest_prime_factor(number, largest_prime_factor=1)
che calcoli e ritorni il più grande fattore primo del numero dato."""

def find_largest_prime_factor(number, largest_prime_factor=1):
    if number is not largest_prime_factor:
        find_largest_prime_factor(number, largest_prime_factor + 1)
        return largest_prime_factor    
    if number is not largest_prime_factor and number%largest_prime_factor is 0:
        find_largest_prime_factor(number, largest_prime_factor + 1)

print(find_largest_prime_factor(4))

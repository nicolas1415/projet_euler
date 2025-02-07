from sympy import isprime
from itertools import permutations

def largest_pandigital_prime(n):
    digits = ''.join(str(i) for i in range(1, n + 1))
    pandigital_numbers = [''.join(p) for p in permutations(digits)]

    for num in sorted(pandigital_numbers, reverse=True):
        if isprime(int(num)):
            return int(num)

n = 7  # 9-digit pandigital
result = largest_pandigital_prime(n)
print(result)

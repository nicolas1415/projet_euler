from sympy import isprime

def is_circular_prime(n):
    n_str = str(n)
    for _ in range(len(n_str)):
        if not isprime(int(n_str)):
            return False
        n_str = n_str[1:] + n_str[0]  # Rotate the digits
    return True

def count_circular_primes(limit):
    circular_primes = [n for n in range(2, limit) if is_circular_prime(n)]
    return len(circular_primes)

limit = 1000000
result = count_circular_primes(limit)
print(result)

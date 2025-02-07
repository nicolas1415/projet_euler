from sympy import isprime

def is_truncatable_prime(n):
    n_str = str(n)
    for i in range(1, len(n_str)):
        if not isprime(int(n_str[i:])) or not isprime(int(n_str[:-i])):
            return False
    return True

def find_truncatable_primes():
    truncatable_primes = []
    num = 10  # Starting from 10 as 2, 3, 5, and 7 are not considered

    while len(truncatable_primes) < 11:
        if isprime(num) and is_truncatable_prime(num):
            truncatable_primes.append(num)
        num += 1

    return truncatable_primes

result = sum(find_truncatable_primes())
print(result)

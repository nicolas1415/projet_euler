from sympy import primerange
import math

def count_expressible_numbers(limit):
    primes = list(primerange(2, int(math.sqrt(limit)) + 1))

    expressible_numbers = set()

    for p4 in primes:
        for p3 in primes:
            for p2 in primes:
                num = p2**2 + p3**3 + p4**4
                if num < limit:
                    expressible_numbers.add(num)

    return len(expressible_numbers)

limit = 50000000
result = count_expressible_numbers(limit)

print(f"The number of expressible numbers below {limit} is: {result}")

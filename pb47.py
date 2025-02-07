def distinct_prime_factors_count(n):
    factors = set()
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.add(i)
    if n > 1:
        factors.add(n)
    return len(factors)

def find_consecutive_numbers(target_count):
    consecutive_numbers = []
    current_number = 1

    while True:
        if distinct_prime_factors_count(current_number) == target_count:
            consecutive_numbers.append(current_number)
            if len(consecutive_numbers) == target_count:
                return consecutive_numbers
        else:
            consecutive_numbers = []
        
        current_number += 1

# Find the first four consecutive integers with four distinct prime factors each
result = find_consecutive_numbers(4)

print("The first four consecutive integers with four distinct prime factors each are:", result)
print("The first number in this sequence is:", result[0])


from decimal import Decimal, getcontext

def digital_sum(number):
    # Convert the number to a string and sum its digits
    return sum(int(digit) for digit in str(number).replace('.', '')[:100])

def find_digital_sums(limit):
    # Set decimal precision to a sufficiently high value
    getcontext().prec = 102

    total_digital_sum = 0

    for n in range(1, limit + 1):
        # Check if the square root is not an integer
        if int(n**0.5)**2 != n:
            # Calculate the square root using Decimal to maintain precision
            root = Decimal(n).sqrt()
            print(root)
            # Calculate the digital sum and add it to the total
            total_digital_sum += digital_sum(root)

    return total_digital_sum

# Find the total of digital sums for the first one hundred natural numbers
result = find_digital_sums(100)

print("Total of the digital sums:", result)

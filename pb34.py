import math

def factorial(n):
    return math.factorial(n)

def sum_of_factorial_digits(number):
    return sum(factorial(int(digit)) for digit in str(number))

def find_digit_factorial_sums():
    digit_factorial_sums = []

    # Upper limit: Since 9! * 7 = 2540160, a 7-digit number is an upper limit for consideration
    for num in range(10, 2540161):
        if num == sum_of_factorial_digits(num):
            digit_factorial_sums.append(num)

    return digit_factorial_sums

result = sum(find_digit_factorial_sums())
print(result)

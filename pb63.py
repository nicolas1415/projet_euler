def count_digit_powers(n):
    count = 0
    limit = 10**(n-1)  # Minimum n-digit number
    upper_limit = int(10**(n/float(n-1)))  # Upper limit to iterate through

    for base in range(1, upper_limit):
        power = base ** n
        if len(str(power)) == n:
            count += 1

    return count

# Set the value of n
n_value = 5

# Find the number of n-digit positive integers that are also an nth power
result = count_digit_powers(n_value)
print(f'The number of {n_value}-digit positive integers that are also an {n_value}-th power is:', result)

s = 0
for n in range(2,2000) :
    s+=count_digit_powers(n)
print(s)
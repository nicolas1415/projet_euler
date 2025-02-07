import math

def is_pentagonal(n):
    # Check if a number is pentagonal
    x = (1 + math.sqrt(1 + 24 * n)) / 6
    return x.is_integer()



for n in range(287,100000,2) :
    number = int(n*(n+1)/2)
    if is_pentagonal(number) :
        print(number)
        break
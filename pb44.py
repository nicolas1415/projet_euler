import math

def is_pentagonal(n):
    # Check if a number is pentagonal
    x = (1 + math.sqrt(1 + 24 * n)) / 6
    return x.is_integer()

def find_minimized_pentagonal_pair():
    min_difference = float('inf')

    for j in range(1, 10000):
        pj = j * (3 * j - 1) // 2

        for k in range(j + 1, 10000):
            pk = k * (3 * k - 1) // 2

            if is_pentagonal(pj + pk) and is_pentagonal(pk - pj):
                difference = abs(pk - pj)
                if difference < min_difference:
                    min_difference = difference
                    result = (pj, pk)

    return result

minimized_pair = find_minimized_pentagonal_pair()
print("The pair of pentagonal numbers with minimized difference is:", minimized_pair)
print("Their difference (D) is:", abs(minimized_pair[1] - minimized_pair[0]))

def count_solutions(p):
    count = 0
    for a in range(1, p // 3 + 1):
        b = (p**2 - 2*p*a) / (2*p - 2*a)
        c = p - a - b

        if b.is_integer() and b > 0 and c > 0:
            count += 1

    return count

def find_max_solutions_perimeter(limit):
    max_solutions = 0
    max_solutions_perimeter = 0

    for p in range(2, limit + 1, 2):  # Perimeter is even
        solutions = count_solutions(p)
        if solutions > max_solutions:
            max_solutions = solutions
            max_solutions_perimeter = p

    return max_solutions_perimeter

limit = 1000
result = find_max_solutions_perimeter(limit)
print(result)

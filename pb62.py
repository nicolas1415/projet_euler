from collections import defaultdict

def find_smallest_cube(target_permutations):
    cube_dict = defaultdict(list)
    n = 1

    while True:
        cube = n ** 3
        sorted_digits = ''.join(sorted(str(cube)))
        cube_dict[sorted_digits].append(cube)

        if len(cube_dict[sorted_digits]) == target_permutations:
            return min(cube_dict[sorted_digits])

        n += 1

# Find the smallest cube for which exactly five permutations of its digits are cube
result = find_smallest_cube(5)
print("The smallest cube is:", result)

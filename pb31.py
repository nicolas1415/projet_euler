from itertools import permutations

def is_pandigital(s):
    return ''.join(sorted(s)) == '123456789'

def find_pandigital_products_sum():
    pandigital_products = set()

    for perm in permutations('123456789'):
        perm_str = ''.join(perm)

        # Check all possible combinations of multiplicand and multiplier
        for i in range(1, 5):
            for j in range(i + 1, 6):
                multiplicand = int(perm_str[:i])
                multiplier = int(perm_str[i:j])
                product = int(perm_str[j:])

                if multiplicand * multiplier == product:
                    pandigital_products.add(product)

    return sum(pandigital_products)

result = find_pandigital_products_sum()
print(result)
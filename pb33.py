from fractions import Fraction

def find_curious_fractions():
    curious_fractions = []

    for numerator in range(10, 100):
        for denominator in range(numerator + 1, 100):  # Ensure denominator > numerator
            common_digits = set(str(numerator)) & set(str(denominator))

            if len(common_digits) == 1 and '0' not in common_digits:
                common_digit = common_digits.pop()

                # Remove common digit and check if the fraction is equal to the simplified form
                numerator_str = str(numerator).replace(common_digit, '')
                denominator_str = str(denominator).replace(common_digit, '')

                if numerator_str == '' :
                    numerator_str += common_digit
                if denominator_str =='':
                    denominator_str += common_digit

                if int(denominator_str) != 0 :
                    simplified_fraction = Fraction(int(numerator_str), int(denominator_str))

                    if Fraction(numerator, denominator) == simplified_fraction:
                        curious_fractions.append(Fraction(numerator, denominator))

    return curious_fractions

curious_fractions = find_curious_fractions()
print(len(curious_fractions))

# Calculate the product of the four fractions in their lowest common terms
product_fraction = Fraction(1, 1)
for fraction in curious_fractions:
    product_fraction *= fraction

# Print the denominator of the product in its lowest common terms
print(product_fraction.denominator)

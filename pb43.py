

def isPandigital(number) :
    histo = [0]*10
    for chiffre in number :
        histo[int(chiffre)] += 1
    S = 0 
    for elem in histo :
        S += (elem==1)
    return S==10


def test(number) :
    return isPandigital(number)*(int(number[1:4])%2 ==0 )*(int(number[2:5])%3 ==0 )*(int(number[3:6])%5 ==0 )*(int(number[4:7])%7 ==0 )*(int(number[5:8])%11 ==0 )*(int(number[6:9])%13 ==0 )*(int(number[7:])%17 ==0 )


print(test('1406357289'))


from itertools import permutations

# Generate all pandigital numbers (0-9)
digits = '0123456789'
pandigital_numbers = [''.join(p) for p in permutations(digits)]
S=0
for pan in pandigital_numbers :
    if test(pan) :
        S+= int(pan)

print(S)
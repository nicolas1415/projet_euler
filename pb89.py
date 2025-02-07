
Romans = ['I','V','X','L','C','D','M']

with open('romans.txt','r') as file :
    Input = file.read()
    Input = Input.split('\n')

print(Input)


import time
import sys


def replace_all(text, dic):
    for i, j in dic.items():
        text = text.replace(i, j)
    return text


def main():
    start = time.perf_counter()
    a = open("romans.txt").read()
    reps1 = {'DCCCC': 'CM', 'LXXXX': 'XC', 'VIIII': 'IX'}
    reps2 = {'CCCC': 'CD', 'XXXX': 'XL', 'IIII': 'IV'}
    new = replace_all(replace_all(a, reps1), reps2)
    print(len(a) - len(new))
    print('temps d\'exécution', time.perf_counter() - start, 'sec')

if __name__ == '__main__':
    sys.exit(main())
import math

def is_pentagonal(n):
    # Check if a number is pentagonal
    x = (1 + math.sqrt(1 + 24 * n)) / 6
    return x.is_integer()

def is_square(n) :
    x = math.sqrt(n)
    return x.is_integer()

def is_hexagonal(n) :
    x = (1 + math.sqrt(1 + 8 * n)) / 4
    return x.is_integer()

def is_septonal(n) :
    x = (3 + math.sqrt(9 + 40 * n)) / 10
    return x.is_integer()

def is_octogonal(n) :
    x = (1 + math.sqrt(1 + 3 * n)) / 3
    return x.is_integer()

def doingtest(n,index) :
    if index == 0 :
        return is_square(n)*1
    elif index == 1 :
        return is_pentagonal(n)*1
    elif index == 2 :
        return is_hexagonal(n)*1
    elif index == 3 :
        return is_septonal(n)*1
    else :
        return is_octogonal(n)*1


def main() :
    S = 0
    N = int(math.sqrt(20000))
    for n in range(46,N,2) :
        tests = [0]*5
        number = int(n*(n+1)/2)
        number_str = str(number)
        lst_numbers = [number_str]
        lst_last = [[number_str, tests, lst_numbers]]
        for index in range(1,5) :
            lst_temp = []
            for i in range(10,100) :
                for elem in lst_last :
                    if i %10 != 0:
                        new_number = elem[0][2:]  +str(i)
                        tests_temp = [0]*5
                        for k in range(5) :
                            if doingtest(int(new_number),k) + elem[1][k]<2 :
                                tests_temp[k] = doingtest(int(new_number),k) + elem[1][k]
                        if sum(tests_temp) == index :
                            lst_numbers = elem[2].copy()
                            lst_numbers.append(new_number)
                            lst_temp.append([new_number,tests_temp,lst_numbers])
            lst_last = lst_temp.copy()

        lst_temp = []
        for elem in lst_last :
            new_number = elem[0][2:] + elem[2][0][:2]
            tests_temp = [False]*5
            for k in range(5) :
                if doingtest(int(new_number),k) + elem[1][k]<2 :
                    tests_temp[k] = doingtest(int(new_number),k) + elem[1][k]
            if sum(tests_temp) == 5 :
                lst_numbers = elem[2].copy()
                lst_numbers.append(new_number)
                lst_temp.append([new_number,tests_temp,lst_numbers])
        lst_last = lst_temp.copy()
        if len(lst_last) != 0 :
            S = 0
            for string in lst_last[0][2] :
                print(string)
                S+=int(string)

            print(S)
            return

main()
    
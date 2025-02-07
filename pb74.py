

def facto(n) :
    prod = 1
    if n == 0:
        return 1
    for i in range(1,n+1) :
        prod*=i
    return prod

def goingOneStep(number) :

    S = 0
    for letter in number :
        S += facto(int(letter))
    return str(S)


def gettingValueLoop(nbr) :
    lst = []
    d_nbr = str(nbr)
    while not d_nbr in lst :
        lst.append(d_nbr)
        d_nbr = goingOneStep(d_nbr)
    return len(lst)


def main(D = 1000000):
    count = 0
    for d in range(1,D+1) :
        loopValue = gettingValueLoop(d)
        if loopValue == 60 :
            count += 1
    print(count)
    return


if __name__ == "__main__" :
    main()
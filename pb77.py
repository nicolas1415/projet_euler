
def primes(n) :

    elem = [1] *n
    elem[0] = 0

    for i in range(1,n) :
        if elem[i] == 1 :
            index = (i+1)*2
            while index <= n:
                elem[index-1] = 0
                index += (i+1)

    primes = []
    for index, value in enumerate(elem) :
        if value ==1 :
            primes.append(index+1)
    return primes

def gettingNbr(n) :
    prime_vals = primes(n)
    ways = [0]*(n+1)
    ways[0] = 1

    for i in range(len(prime_vals)) :
        for j in range(prime_vals[i],n+1) :
            ways[j] += ways[j-prime_vals[i]]
    return ways[n]


def main() :
    n=10
    while gettingNbr(n) <= 5000 :
        n+=1
    print(gettingNbr(n))
    print(n)
    return

if __name__ == "__main__" :
    main()
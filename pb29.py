

def compute(a = 100, b = 100) :
    aList = []
    for a_prime in range(2,a+1) :
        for b_prime in range(2,b+1) :
            aList.append(a_prime**b_prime)
    return aList

def main() :
    List = compute()
    List = sorted(List)
    List = list(set(List))
    print(len(List))

if __name__ == "__main__" :
    main()
    


class Frac :

    def __init__(self,x,y) :
        self.x = x
        self.y = y


    def __lt__(self, other) :
        return self.x*other.y < other.x*self.y
    

def pgcd(x,y) :
    while y!=0 :
        x,y = y,x%y
    return x


def main(D = 12000) :

    elem_frac1 = Frac(1,2)
    elem_frac2 = Frac(1,3)
    count  = 0 

    for d in range(4,D+1) :
        if d%1000 == 0 :
            print('work in progress')
        for x in range(1,d) :
            if pgcd(d,x) == 1 :
                elem = Frac(x,d)
                if elem_frac2 < elem < elem_frac1 :
                    count += 1
    print(count)
    return

if __name__ == "__main__" :
    main()
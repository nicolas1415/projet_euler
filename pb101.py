
class Lagrange :

    def __init__(self, deg, racines, values) :
        
        self.deg = deg
        self.racines = racines.copy()
        self.values = values.copy()

    def getValue(self,i, x) :

        prod = 1
        div = 1
        for j in range(len(self.racines)) :
            if i!= j :
                prod*=(x-self.racines[j])
                div *= (self.racines[i]-self.racines[j])
        return prod/div
    
    def computeTerm(self,n) :
        Sum = 0
        for j in range(len(self.racines)) :
            Sum += self.values[j]*self.getValue(j,n)
        return Sum

def u_n(n) :
    return (n**11 + 1)/(n+1)


def main() :
    Sum = 1
    racines = [1,2]
    values = [1,u_n(2)]
    for i in range(9) :
        L = Lagrange(i+1,racines,values)
        elem = len(racines)
        racines.append(elem+1)
        values.append(u_n(elem+1))
        while L.computeTerm(elem+1) == u_n(elem+1) :
            elem += 1
        Sum += L.computeTerm(elem+1)

    print(Sum)

main()
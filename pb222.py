
def permutations(n) :
    if n == 1 : 
        return [[1]]
    else :
        set_permutation = permutations(n-1)
        new_set_of_permutations = []
        for i in range(n) :
            for sigma in set_permutation :
                sigmacop = sigma.copy()
                sigmacop.insert(i,n)
                new_set_of_permutations.append(sigmacop)
        return new_set_of_permutations
    

permutations(10)
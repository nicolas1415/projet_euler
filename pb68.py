

import time

def permutations(n) :
    if n==1 :
        return [[1]]
    else :
        perms = permutations(n-1)
        res = []
        for i in range(n) :
            for mu in perms :
                elem = mu.copy()
                elem.insert(i,n)
                res.append(elem)
        return res

def secondTesting(mu) :
    if mu[5] > mu[6] :
        return False
    if mu[5] > mu[7] :
        return False
    if mu[5] > mu[8] :
        return False
    if mu[5] > mu[9] :
        return False
    return True

def testing(mu) :
    first = mu[0] + mu[5] + mu[1]
    second = mu[1] + mu[2] + mu[6]
    third = mu[2] + mu[3] + mu[7]
    forth = mu[3] + mu[4] + mu[8]
    fif = mu[4] + mu[0] + mu[9]

    return (first==second)*(first==third)*(first==forth)*(first==fif)

def getString(mu) :
    string = ''
    string += str(mu[5]) +str(mu[0])+ str(mu[1])
    string += str(mu[6]) +str(mu[1])+ str(mu[2])
    string += str(mu[7]) +str(mu[2])+ str(mu[3])
    string += str(mu[8]) +str(mu[3])+ str(mu[4])
    string += str(mu[9]) +str(mu[4])+ str(mu[0])
    return string

t1 = time.time()
H = permutations(10)
for mu in H :
    if secondTesting(mu) :
        if testing(mu) == 1:
            elem = getString(mu)
            if len(elem) == 16 :
                print(elem)
t2 = time.time()

print(t2-t1)
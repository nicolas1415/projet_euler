

def isPandigital(number) :
    histo = [0]*9
    for chiffre in number :
        if int(chiffre) == 0:
            return False
        else :
            histo[int(chiffre) -1] += 1
    S = 0 
    for elem in histo :
        S += (elem==1)
    return S==9


for k in range(9111,10000) :
    number = ''
    for i in range(2) :
        number += str(k*(i+1))
    if isPandigital(number) :
        print(number)
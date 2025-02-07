
def counting(n) :
    S = 1
    N = 1
    for k in range(1,n+1) :
        for i in range(4) :
            N += 2*k
            S += N


    return S

print(counting(500))

                
        
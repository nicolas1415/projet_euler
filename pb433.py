
import numpy as np 

def E(x,y) :
    a,b = x,y
    n = 0
    while b!=0 :
        a,b = b, a%b
        n += 1
    return n



def E_memo(x,y, numpy_array) :
    if numpy_array[x-1,y-1] != -1 :
        return numpy_array[x-1,y-1]

    else :
        if x%y == 0 :
            numpy_array[x-1,y-1] = 1
        else :
            numpy_array[x-1,y-1] = 1 + E_memo(y, x%y, numpy_array)
        return numpy_array[x-1,y-1]


def S(N) :
    S = 0
    arr = np.zeros((N,N), dtype= np.int16)
    arr [:,:] = -1
    arr[:,0] = 1
    for x in range(2,N+1) :
        for y in range(1,x) :
            S += 2*E_memo(x,y,arr) + 1
    S += N
    return S  

print(S(int(5*1e4)))
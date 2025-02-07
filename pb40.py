
def getList(d = 1000000) :
    i = 1
    aList = []
    while len(aList) <d :
        k = i
        elem = []
        while k!=0 :
            elem.insert(0,k%10)
            k = k//10
        aList += elem
        i += 1
    return aList

H = getList()
prod = H[0]*H[9]*H[99]*H[999]*H[9999]*H[99999]*H[999999]
print(prod)
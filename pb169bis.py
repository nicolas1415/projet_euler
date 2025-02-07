
def findIndexes(n) :
    aList = []
    while n!=0 :
        if n%2 != 0:
            n = n//2
            aList.insert(0,n)
        else :
            over = n//2
            under = n//2-1
            aList.insert(0,over)
            aList.insert(0,under)
            if over % 2 == 0:
                n = over
            else :
                n = under
    return aList

def f(n) :
    aList = findIndexes(n)
    values = []
    for (index,elem) in enumerate(aList) :
        if index < 2:
            values.insert(0,1)
        else :
            if elem % 2==0 :
                values.append(values[index-1] +values[index-2])
            else :
                values.append(values[index-2])
    if n%2 == 0:
        return values[-1] + values[-2]
    else :
        return values[-1]

print(f(int(10000000000000000000000000)))
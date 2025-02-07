

def pgcd(x,y) :
    while y!=0:
        x,y = y,x%y
    return x


def computingList(D) :
    aList = [0]*(D-1)
    for d in range(2,D+1) :
         aList[d-2] += d-1
         index = 2*d 
         while index <= D :
             aList[index-2] -= aList[d-2]
             index += d

    return aList, sum(aList)


        



def main( D= 1000000) :

    elem, count = computingList(D)

    print(count)
    return

if __name__ == "__main__" :
    main(D = 12000)


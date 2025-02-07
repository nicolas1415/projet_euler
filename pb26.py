

def gettingList(d) :

    aList = []
    listOfRest = []
    elem = 10


    index  = 0
    while elem != 0 and index < 3000:
        index += 1
        aList.append(elem // d)
        listOfRest.append(elem%d)
        elem = 10 * (elem%d)
    return aList, listOfRest

#print(gettingList(7))

def main(d = 1000) :

    max_d = 2
    max_count = 1

    for elem in range(2,d) :
        aList, listR = gettingList(elem)
        temp_list = []
        index = 0
        if elem%2 !=0 and elem%5 != 0:
            while not listR[index] in temp_list :
                temp_list.append(listR[index])
                index += 1
            count = len(temp_list)
        else :
            count = 0
        if count >= max_count :
            max_count = count 
            max_d = elem

    print(max_count)
    print(max_d)
    return 

if __name__ == "__main__" :
    main(d = 1000)

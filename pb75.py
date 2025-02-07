import math

def pgcd(x,y) :
    while y!=0 :
        x,y = y,x%y
    return x

def main(D = 1500000) :

    max_value_m = 1 + int(math.sqrt(D/2))
    values =[0] * D

    for m in range(2,max_value_m) :
        max_n = min(int(D/(2*m) - m +1),m)
        if m%2 == 0:
            for n in range(1,max_n,2) :
                if pgcd(m,n) == 1 :
                    number = 2*m*(m+n)
                    copy = number
                    while number <= D :
                        values[number -1] += 1
                        number += copy
                    
        else :
            for n in range(2,max_n,2) :
                if pgcd(m,n) == 1 :
                    number = 2*m*(m+n)
                    copy = number
                    while number <= D :
                        values[number -1] += 1
                        number += copy

    
    count = 0
    for value in values :
        if value == 1 :
            count += 1
    return count


print(main())
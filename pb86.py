import math
def count_sol(M) :
    count = 0
    for a in range(1,M+1) :
        for b in range(1,a+1) :
            for c in range(1,b+1) :
                if math.sqrt(a**2 + (b+c)**2).is_integer() :
                    count += 1
    return count

def adding_sol(M) :
    count = 0
    for b in range(1,M+1) :
        for c in range(1,b+1) :
            if math.sqrt(M**2 + (b+c)**2).is_integer() :
                count += 1
    return count

M =1
count = count_sol(M)
print(count)
while count < 2000 :
    count += adding_sol(M)
    M += 1

print(M)


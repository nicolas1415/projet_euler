import numpy as np

def countDifferentLines(n) :
    if n <= 1 :
        return 0
    elif n == 2 :
        return 1
    elif n == 3 :
        return 1
    else :
        return countDifferentLines(n-2) + countDifferentLines(n-3)
    

def computeLines(n):
    if n <= 0:
        return []
    elif n == 2:
        return [np.array([2])]
    elif n == 3:
        return [np.array([3])]
    
    elem = computeLines(n - 2)
    if len(elem) > 0 :
        elem = [np.concatenate([[2], e]) for e in elem]
    
    elem2 = computeLines(n - 3)
    if len(elem2) > 0 :
        elem2 = [np.concatenate([[3], e]) for e in elem2]

    return elem + elem2

def testingCompatibillity(firstarray, secondarray) :
    p = 1
    q = 1
    a = firstarray.size
    b = secondarray.size
    while p != a or q!=b :
        val1 = np.sum(firstarray[:p])
        val2 = np.sum(secondarray[:q])
        if val1 == val2 :
            return False
        elif val1 < val2 :
            p+=1
        else :
            q+=1
    return True

def computingMatrix(n) :
    matrix_size = countDifferentLines(n)

    matrix_size_axis1 = countDifferentLines(n-2)
    matrix_size_axis2 = countDifferentLines(n-3)

    lines = computeLines(n)

    matrix  = np.zeros((matrix_size,matrix_size))

    for i in range(matrix_size) :
        for j in range(matrix_size) :
            if testingCompatibillity(lines[i], lines[j+matrix_size_axis1]) :
                matrix[i][j] = 1

    return matrix

#print(testingCompatibillity(np.asarray([2,2,2,3]), np.asarray([3,3,3])))
#print(computeLines(9))
#print(computingMatrix(9))

def W(n,p) :
    if p == 1 :
        return countDifferentLines(n)
    else :
        matrix = computingMatrix(n)
        print("matrix computed")
        result = np.linalg.matrix_power(matrix, p-1)
        return int(np.sum(result))
    
print(W(32,10))


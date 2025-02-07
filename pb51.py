import time
# global vars
start = time.time()
wildcards = []
primes = []
primes.append(2)

# generate every possible wildcard strings
def genWildcardStrings(s, index):
    if index > 0:
        wildcards.append(s)
    for x in range(index, len(s)):
        genWildcardStrings(createPlaceholder(s, x), x+1)

# replace a character with '*'
def createPlaceholder(s, index):
    return s[0:index] + '*' + s[index+1:]
# binarysearch for searching prime
def binarySearch(prime):
    start = 0
    end = len(primes)
    middle = int((end + start)/2)
    
    while(start < end 
          and primes[middle] != prime 
          and middle < len(primes)):
        if primes[middle] < prime:
            start = middle+1
        else:
            end = middle-1
        middle = int((end + start)/2)
    
    if middle < len(primes) and primes[middle] == prime:
        return middle
    else:
        return -1
# lets go and find primes from 3-1000000
for x in range(3, 1000000):
    found = False
    for i in range(0, len(primes)):
        if x % primes[i] == 0:
            found = True
            break
        if primes[i] * primes[i] > x:
            break
    if not found:
        primes.append(x)
# loop through primes
for x in range(0, len(primes)):
    wildcards = []
    # generate all possible wildcard strings for that prime
    genWildcardStrings(str(primes[x]), 0)
    # loop through all possible wildcard strings
    for y in range(1, len(wildcards)):
        count = 0
        # fill up the asterisk with 0-9
        for z in range(0, 10):
            num = int(wildcards[y].replace('*', str(z)))
            if binarySearch(num) >= 0:
                count += 1
        # if counter is at least 8 then print and exit program
        if count >= 8:
            print(primes[x])
            print(wildcards[y])
            print("Elapsed time: " + str(time.time() - start))
            exit(0)
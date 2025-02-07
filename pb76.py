
import time   

def count(value, ns):
	ways = [1]+[0]*value
 
	for n in ns:
		for i in range(n, value+1):
			ways[i] += ways[i-n]
 
	return ways

def solve():
	value = 100000
	S = range(1, value)

	elem = count(value, S)
	print(elem[5])
	index = 1
	while (elem[index])%1000000 != 0:
		index += 1
	print(index)

if __name__=="__main__":
	start = time.time()
	solve()
	print("Elapsed Time:", (time.time() - start), "sec")
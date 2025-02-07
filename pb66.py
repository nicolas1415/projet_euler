import math
import time

def getMinSol(d):
	# find period of continued fraction convergents to sqrt(d)
	la = []
	m0 = 0
	d0 = 1
	a0 = int(math.floor(math.sqrt(d)))
	la.append(a0)
	
	li = []
	li.append((m0, d0, a0))
	
	m1 = d0*a0-m0
	d1 = (d-m1*m1)/d0
	a1 = int(math.floor((math.sqrt(d)+m1)/d1))
	la.append(a1)
	
	while (m1, d1, a1) not in li:	
		li.append((m1, d1, a1))
		m0, d0, a0 = m1, d1, a1
		m1 = d0*a0-m0
		d1 = (d-m1*m1)/d0
		a1 = int(math.floor((math.sqrt(d)+m1)/d1))
		la.append(a1)
	la = la[:len(la)-1]
	#print la
	
	# compute minimum solution in x
	# r odd: (pr, qr)
	# r even: (p2r+1, q2r+1)
	
	ret = 0
	r = len(la) - 2
	if r%2 == 1:
		# r odd
		pn, qn = 0, 0
		p0 = la[0]
		q0 = 1
		p1 = la[0]*la[1]+1
		q1 = la[1]
		for i in range(2, r+1):
			pn = la[i]*p1 + p0
			qn = la[i]*q1 + q0 
			p0, q0 = p1, q1
			p1, q1 = pn, qn
		if r == 1:
			#print "r odd:", r, "min sol:", p1, q1
			ret = p1
		else:
			#print "r odd:",r, "min sol:", pn, qn
			ret = pn
	else:
		# r even
		for i in range(1, len(la)*3):
			la.append(la[i])
#		print "la: ", la
		pn, qn = 0, 0
		p0 = la[0]
		q0 = 1
		p1 = la[0]*la[1]+1
		q1 = la[1]
		for i in range(2, 2*r+2):
			pn = la[i]*p1 + p0
			qn = la[i]*q1 + q0 
			p0, q0 = p1, q1
			p1, q1 = pn, qn
		if 2*r+1 == 1:
			#print "r even", r, "min sol:", p1, q1
			ret = p1
		else:
			#print "r even:",r, "min sol:", pn, qn
			ret = pn
	return ret 				
	
def solve():
	maxi, D  = 0, 0
	for i in range(2, 1000+1):
		if i-int(math.sqrt(i))*int(math.sqrt(i)):
			x = getMinSol(i)
			if x > maxi:
				maxi = x
				D = i
	print (maxi, D)
		
if __name__ == "__main__":
	start = time.time()
	solve()
	print("Elapsed Time:", (time.time() - start), "sec")
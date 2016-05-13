#Austin Russell
#11/5/15

# Find the thirteen adjacent digits in the 1000-digit number that have
# the greatest product. What is the value of this product?

import sys

string = sys.argv[1]
opend = open(string)

high = 0
numstore = []

def mult(l1):
	tots = 1
	for i in range(len(l1)):
		tots = tots*l1[i]
		i+= 1
	return tots

for i in range(53):
	rea = opend.readline(i)
	for lines in rea:
		if lines.strip():
			n = int(lines)
			numstore.append(n)

for i in range(len(numstore)):
	sum1 = numstore[i:13 + i]
	prod1  = mult(sum1)
	
	sum2 = numstore[i+1:14 +i]
	prod2 = mult(sum2)
	
	if prod1 > prod2 and prod1 > high:
		high = prod1
		i += 1
	elif prod1 < prod2 and prod2 > high:
		high = prod2
		i += 1
	else:
		i += 1
print high


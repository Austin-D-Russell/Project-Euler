# Austin Russell
# 11/13/15

# Highest product of 4 numbers in a 20X20 grid in the same direction

import sys

string = sys.argv[1]
opend = open(string)

arrayList = []
for line in opend.readlines():
    arrayList.extend(line.split())
opend.close()
arrayList = map(int, arrayList)

def row (x):
	Original = x
	high = 0
	for i in range(397):
		tot = Original[i]* Original[i+1]* Original[i+2]* Original[i+3]
		if tot > high:
			high = tot
			i += 1
		else:
			i+= 1
	return high

def col (x):
	Original = x
	high = 0
	for i in range(340):
		tot = Original[i]* Original[i+20]* Original[i+40]* Original[i+60]
                if tot > high:
                        high = tot
                        i += 1
                else:
                        i+= 1
        return high

def rdiag (x):
	original  = x
	high = 0
	for i in range(337):
		tot = original[i]* original[i+21]* original[i+42]* original[i+63]
		if tot > high:
			high = tot
			i += 1
		else:
			i += 1
	return high

def ldiag (x):
	original  = x
	high = 0
	for i in range(337):
		tot = original[i+3]* original[i+22]* original[i+41]* original[i+60]
		if tot > high:
			high = tot
			i += 1
		else:
			i += 1
	return high
	
sum1 = col(arrayList)
sum2 = row(arrayList)
sum3 = rdiag(arrayList)
sum4 = ldiag(arrayList)


print max(sum1,sum2,sum3,sum4)

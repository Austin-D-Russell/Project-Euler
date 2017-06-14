a1 = 1
a2 = 1
count = 2

while (True):
	count += 1
	val = a1+a2
	a1 = a2
	a2 = val
	if(len(str(val)) == 1000):
		print count
		break
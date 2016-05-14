# Austin Russell
# 11/26/15
# What is the value of the first triangle number to have over five hundred divisors 

#helper function for factoring
def factor(num):
	arr = []
	for n in range(1, num): 
		if num % n == 0:
			arr.append(n)
			n += 1
		else:
			n += 1
	return len(arr)

trianglenumber = 1
value  = 0
Numberfactor = factor(trianglenumber)

# while the value of factor is greater than or equal to 500 
while (Numberfactor <= 500):
	trianglenumber += 1
	value = value + trianglenumber
	Numberfactor  = factor(value) 
	print "Triangle:" 
	print  value
	print "Factors:"
	print  Numberfactor


# update triangle number 
# update factor

print trianglenumber

#print Triangle number
	

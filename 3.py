#Austin Russell
#11/5/15

#What is the largest prime factor of the number 600851475143


factors = []
primes = []


found = False
i =2
x = 600851475143


def is_prime(y):
	a = 2
	while y > a:
		if y%a==0:
			return False
		a += 1	
	else: 
		return True
			
 
    
while( found == False):
	if x%i == 0:
		val = x/i
		factors.append(i)
		factors.append(val)
		if is_prime(val) == True:
			print val
			found = True
		else:
			i =i + 1
	else:
		i = i+1

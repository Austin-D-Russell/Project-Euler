#Austin Russell
#11/5/15

#What is the 10 001st prime number?

primes = []
i = 2

def is_prime(y):
	a = 2
	while y > a:
		if y%a==0:
			return False
		a += 1	
	else: 
		return True

while (len(primes) < 10001):
	if is_prime(i) == True:
		primes.append(i)
		i += 1
	else:
		i += 1

print primes[-1]

#Austin Russell
#11/7/15

#Find the sum of all the primes below two million.
#works but is really slow

prime = []

def is_prime(y):
	a = 2
	while y > a:
		if y%a==0:
			return False
		a += 1
	return True

for i in range(2,2000000):
	if is_prime(i) == True:
		prime.append(i)
		i += 1
		print prime[-1]
	else:
		i += 1
print sum(prime)



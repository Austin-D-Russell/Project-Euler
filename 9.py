#Austin Russell
#11/5/15

# a**2 + b**2 = c**2, a < b < c

#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc

import math
a = 500
b = 1

inequal = True

while (inequal == True):
	c = math.sqrt(a**2+b**2)
	if a+b+c < 1000:
		b += 1
	elif a+b+c == 1000 and a**2+b**2==c**2:
		#print a,b,c
		print a*b*c
		#print a+b+c
		#print a**2,b**2,c**2
		inequal = False
	else:
		a -= 1

#attempt 1
'''


a = 3
b = 4
c = 5
	
inequal = True


while (inequal == True):
	if (a**2 + b**2)==(c**2):
		if b > a +1:
			if ( a+b+c == 1000):
				inequal = False
			pow_c = a**2 + b**2
			c = math.sqrt(pow_c)
			a += 1 
			print "ok"
		else:
			if ( a+b+c == 1000):
				inequal = False
			pow_c = a**2 + b**2
			c = math.sqrt(pow_c)
			b += 1
			print"not bad"

	else:
		pow_c = a**2 + b**2
		c = math.sqrt(pow_c)
		if b > a + 1:
			a += 1 
			print "got"
		else:
			b += 1
			print "ya"

print a,b,c
print a*b*c
print a+b+c
print a**2,b**2,c**2
print a**2,b**2,c**2
'''

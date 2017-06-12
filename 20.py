import math

factorial = math.factorial(100)
s = 0
while factorial:
	s += factorial % 10
	factorial //= 10

print s
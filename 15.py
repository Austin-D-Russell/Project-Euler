#Austin Russell
#6/14/16
#Number of Routes from top left to bottom right on a 20/20 Grid

#using Combinetrics

# (2n)! / n! x n!

#factorial fucntion
def factorial(num):
	if num == 0:
		return 1
	else:
		return num * factorial(num-1)
	
#Size of Square Grid	
n = 20

#Calculate top of Equation
topsum = 2*n
top = factorial(topsum)

#Calculate Bottom of equation
bottomfactorial = factorial(n)
bottom = bottomfactorial * bottomfactorial

#Solve Equation
total = top/bottom

print total

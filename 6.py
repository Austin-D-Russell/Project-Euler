#Austin Russell
#11/5/15

# Find the difference between the sum of the squares of the first 
# one hundred natural numbers and the square of the sum.

squaresum = []
sumsquare = []

for i in range(1,101):
	squaresum.append(i**2)
	sumsquare.append(i)

small = sum(squaresum)
large = sum(sumsquare)**2

tot = large - small
print tot

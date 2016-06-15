#Austin Russell
#6/14/16
#Calculate the sum of the digits from 2^1000

num = 2**1000
numtostring = str(num)
arr = []

for digit in numtostring:
	arr.append(int(digit))

printval = sum(arr)

print printval
	

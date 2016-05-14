#Austin Russell
#5/13/16
#Which starting number, under one million, produces the longest chain?

#list of chain lengths
maxlist  = []

#algorithm for even numbers
def ifeven (num):
	number = num/2
	return number

#algorithm for odd numbers
def ifodd (num):
	number  = 3*num + 1
	return number

#creates chain and returns the length of chain appending to maxlist list
def longestchain (num):
	arrchain.append(num)
	if (num != 1):
		if num % 2 == 0: 
			num = ifeven(num)
			longestchain(num)
		else:
			num = ifodd(num)
			longestchain(num)
	else:
		maxlist.append(len(arrchain))
		return len(arrchain)

#for every element under one million
for i in range(1,1000000):
	#init new chain
	arrchain = []
	#find length of chain
	longestchain(i)

#print the index number of the largest element in the chain length array
#plus one to offset 0th index
print maxlist.index(max(maxlist)) + 1

#Austin Russell
#11/5/15

# What is the smallest positive number that is evenly divisible by all 
# of the numbers from 1 to 20?


i = 1
posnum = 1
stop = False
while (stop == False):
	if posnum % i == 0:
		if i >= 10:
			print i , "  Number:" , posnum
		if i == 20:
			stop = True
			print posnum
		i += 1
	else:
		posnum += 1
		i = 1

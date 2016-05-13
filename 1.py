#Austin Russell
#11/4/15
#Find the sum of all the multiples of 3 or 5 below 1000

mult_sum=[]
i = 1
while (i < 1000):
	if i % 3 == 0 or i %5 == 0:
		mult_sum.append(i)
		i = i + 1
		tot = max(mult_sum)
	else:
		i = i + 1
		
print sum (mult_sum)	
	


				

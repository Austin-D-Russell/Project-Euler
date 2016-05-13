#Austin Russell
#11/5/15

#Find the largest palindrome made from the product of two 3-digit numbers

pal = []

def is_palan(num):
	str(num)
	if str(num) == str(num)[::-1]:
		return True
	else:
		return False
			
for j in range(100,999):		
	for i in range(100,999):
		tot = i*j
		if is_palan(tot) == False:
			i += 1
		else:
			pal.append(tot)
			i += 1
	j += 1
		
print max(pal)


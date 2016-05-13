#Austin Russell
#11/5/15

#By considering the terms in the Fibonacci sequence whose values do not exceed four 
#million, find the sum of the even-valued terms

fib=[1,2]
tot = [2]
newfib = 0
i = 1

while (fib[i] < 4000000):
	newfib = (fib[i] + fib[i-1])
	fib.append(newfib)
	i = i + 1
	if fib[i] % 2 == 0:
		tot.append(newfib)
	else:
		newfib = (fib[i] + fib[i-1])

print sum(tot)

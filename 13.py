#Austin Russell
#5/13/16
#Work out the first ten digits of the sum of the following one-hundread 50-digit numbers.

#used to read in text file
import sys

#With allows a file to be open and then closed upon completion of the initilization of a 2d array
with open(sys.argv[1], "r") as file:

	#declare arrray/lsit for every element in the file split the line 
	#inside loop converts to int(could have used map)
	#outside loop for every line in the file
	arrraw = [[int(x) for x in line.split()] for line in file]

#map calls sum on every element in zip(*arrraw)
#zip with a dereferanced list (ints) gives the collumns
result = map(sum,zip(*arrraw))

string = str(result)


print string[1:11]

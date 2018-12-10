#Solution to Project Euler 18 and 67

#Algorithm Description:
	# After analysis of the problem I have decided to take a bottom up approach.
	# How you would naturally treat the leaf of a tree knowing that is the final
	# decision means you would take the max value available. we can then roll up
	# the tree to get a sub tree summing the potential values. This will always allow
	# us to take the highest value.

	# EX: 1                 1                1             20
	#    2 3       -->     2  3      -->  16  19   -->   
	#   4 5 6            12 14 16
	#  7 8 9 10

def main():

	fp = openfile("tree.txt")
	filecontents = read_file(fp)
	
	readindex = -1

	leafs = create_array(filecontents[readindex])
	readindex -= 1
	sub_leafs = create_array(filecontents[readindex])

	while((len(filecontents) + readindex) != 0):
		readindex -= 1
		leafs = create_subtree(leafs, sub_leafs)
		sub_leafs = create_array(filecontents[readindex])
	
	return create_subtree(leafs, sub_leafs)


def openfile(filename):
	try: return open(filename)
	except: print("Unable to open file, please check file name"); sys.exit(1)

def read_file(fp):
	try: 
		with fp as f:
			return f.readlines()
	except: print("Unable to read a line of the file"); sys.exit(1)

def create_array(s):
	return list(map(int, s.split()))

def create_subtree(bottom, top):
	for i in range(0, len(top)):
		if (bottom[i] + top[i]) > (bottom[i+1] + top[i]):
			top[i] = bottom[i] + top[i]
		else:
			top[i] = bottom[i+1] + top[i]
	return top

if __name__ == '__main__':
	import sys
	print(main())

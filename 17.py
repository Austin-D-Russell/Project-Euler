#If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, 
#how many letters would be used?

#teen = 4
#twenty = 6
#thirty = 6
#forty = 5
#fifty = 5
#sixty = 5
#seventy = 7
#eighty = 6
#ninty = 5
#hundread = 8
#one = 3
#two = 3
#three = 5
#four = 4
#five = 4
#six = 3
#seven = 5
#eight = 5
#nine = 4
#ten = 3
#eleven = 6
#twelve = 6
#thir = 4
#four = 4
#fif = 3

sum = 0

for counter in range(1,1000)
	l = map(int, str(counter))
	if(len(l) == 4){
		sum += 11
	}
	else if(len(l) == 3){

	}
	else if(len(l) == 2){

	}
	else{
		if(l[0] == 1 || l[0] == 2 || l[0] == 6){
			sum += 3
		}
		if()
	}

#Still in progress
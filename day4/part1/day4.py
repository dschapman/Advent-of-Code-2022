f = open("input.txt","r")
total=0
for line in f.readlines():
	pair = line.rstrip('\n').split(',')
	pair[0] = pair[0].split('-')
	pair[1] = pair[1].split('-')
	range1 = set(range(int(pair[0][0]),int(pair[0][1])+1))
	range2 = set(range(int(pair[1][0]),int(pair[1][1])+1))
	if(range1.intersection(range2) == range1 or range1.intersection(range2) == range2):
		total+=1

print(total)
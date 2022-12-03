f = open("input.txt","r")
total = 0
for line in f.readlines():
	compartmenta =  line[:len(line)//2]
	compartmentb = line[len(line)//2:]
	common = set(compartmenta).intersection(compartmentb).pop()
	if(common.isupper()):
		total+=(ord(common)-38)
	elif(common.islower()):
		total+=(ord(common)-96)
print(total)
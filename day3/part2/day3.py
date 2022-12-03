f = open("input.txt","r")
total = 0
lines = f.readlines()
total_lines = len(lines)
x = 0
while(x < total_lines):
	common = set(lines[x].rstrip('\n')).intersection(lines[x+1].rstrip('\n')).intersection(lines[x+2].rstrip('\n')).pop()
	if(common.isupper()):
		total+=(ord(common)-38)
	elif(common.islower()):
		total+=(ord(common)-96)
	x+=3
print(total)
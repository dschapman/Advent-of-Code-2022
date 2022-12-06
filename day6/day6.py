def part1(input):
	for c in range(0,len(input)-4):
		if len(set(input[c:c+4])) == 4:
			print(c+4)
			break;

def part2(input):
	for c in range(0,len(input)-14):
		if len(set(input[c:c+14])) == 14:
			print(c+14)
			break;

f=open("input.txt","r")
input = f.read()
part1(input)
part2(input)


def day1():
	elves = []
	highest=0
	f = open("input.txt","r")
	elf = 0
	for line in f:
		if line != "\n":
			elf+=int(line)
		else:
			if elf > highest:
				highest = elf
			elves.append(elf)
			elf=0
	return highest

print(day1())


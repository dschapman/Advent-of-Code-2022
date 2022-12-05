def part1(input):
	for instruction in input[1]:
		count = int(instruction[0])
		start = int(instruction[1]) - 1
		finish = int(instruction[2]) -1
		temp = input[0][start][:count]
		input[0][start] = input[0][start][count:]
		for item in temp:
			input[0][finish].insert(0,item)
	output=''
	for stack in input[0]:
		if stack != list():
			output += stack[0]
	print(output.replace('[','').replace(']',''))

def part2(input):
	for instruction in input[1]:
		count = int(instruction[0])
		start = int(instruction[1]) - 1
		finish = int(instruction[2]) -1
		temp = input[0][start][:count]
		input[0][start] = input[0][start][count:]
		input[0][finish] = temp + input[0][finish]
	output=''
	for stack in input[0]:
		if stack != list():
			output += stack[0]
	print(output.replace('[','').replace(']',''))

def split_string(input: str) -> list[str]:
	input
	return [input[i:i + 4].strip() for i in range(0, len(input), 4)]

def parse_input(input: str) -> list[str]:
	output = input.split('\n\n')
	output[0] = list(map(split_string,output[0].split('\n')))
	columns = []
	for i in range(0,len(output[0][0])):
		columns.append([])
	for row in range(0,len(output[0])):
		for item in range(0,len(output[0][row])):
			if output[0][row][item] != '':
				columns[item].append(output[0][row][item])
	output[0] = columns
	output[1] = output[1].split('\n')
	instructions = []
	for instruction in output[1]:
		steps = []
		for step in instruction.split():
			if step.isdigit():
				steps.append(step)
		instructions.append(steps)
	output[1] = instructions
	return output



f = open("input.txt","r")

crates = parse_input(f.read())
#part1(crates)
part2(crates)
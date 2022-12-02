import sys

def rock_paper_scissors(player,outcome):
	scores = {"A": 1, "B":2,"C":3,"X":0,"Y":3,"Z":6}
	wins = {"A":"B","B":"C","C":"A"}
	losses = {"A":"C","B":"A","C":"B"}
	if outcome == 'Y':
		return scores["Y"] + scores[player]
	elif outcome == "X":
		return scores["X"] + scores[losses[player]]
	elif outcome == "Z":
		return scores["Z"] + scores[wins[player]]
	else:
		print("Bad input",file=sys.stderr)

f = open("input.txt","r")
total_score = 0
for line in f.readlines():
	moves = line.split()
	print(moves)
	if len(moves) != 2:
		print("Something went wrong with the number of moves.",file=sys.stderr)
	else:
		total_score += rock_paper_scissors(moves[0],moves[1])

print(total_score)

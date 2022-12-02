import sys

def rock_paper_scissors(p1,p2):
	scores = {"A": 1, "B":2,"C":3,"X":1,"Y":2,"Z":3}
	if scores[p1] == scores[p2]:
		return 3 + scores[p2]
	elif p1 == "A" and p2 == "Y":
		return scores[p2] + 6
	elif p1 == "B" and p2 == "Z":
		return scores[p2] + 6
	elif p1 == "C" and p2 == "X":
		return scores[p2] + 6
	else:
		return scores[p2]

f = open("input.txt","r")
total_score = 0
for line in f.readlines():
	moves = line.split()
	if len(moves) != 2:
		print("Something went wrong with the number of moves.",file=sys.stderr)
	else:
		total_score += rock_paper_scissors(moves[0],moves[1])

print(total_score)

import random
import re

Notation = ["R", "R'", "L", "L'", "U", "U'", "F", "F'", "B", "B'"]

def genNew(length):
	Scramble = []
	while len(Scramble) < length:
		Move = random.choice(Notation)
		MoveStr = " ".join(re.findall("[a-zA-Z]+", str(Move)))
		PreviousMove = Scramble[-1:]
		PreviousMove = " ".join(re.findall("[a-zA-Z]+", str(PreviousMove)))
		if MoveStr != PreviousMove:
			Num = random.randint(1,3)
			if Num == 1 or Num == 3:
				Scramble.append(Move)
			else:
				if "'" in str(Move):
					Move = str(Move).replace("'", "")
				Scramble.append('{}2'.format(Move))
	T = ""
	for moves in Scramble:
		T = T + " " + str(moves)
	return T

#http://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html


c=['stone','paper','scissors']

while True:
	a = str(input("Chose you weapone player A"))
	b = str(input("Chose you weapone player B"))
	if (a == "end") or (b == "end"):
		print("Game over")
		break
	else:
		if (a not in c) and (b not in c):
			print("Why u do this")
			continue
		if (a==b):
			print("Draw")
			continue
		if(a == "stone"):
			if (b == "scissors"):
				print("Player A win")
			else
				print("Player A lose")
		if(A == "scissors"):
			if (b == "paper"):
				print("Player A win")
			else
				print("Player A lose")
		if(A == "paper"):
			if (b == "rock"):
				print("Player A win")
			else
				print("Player A lose")

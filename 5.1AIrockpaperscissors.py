from random import randint
# print("Rock...")
# print("Paper...")
# print("Scissors...")
p1 = 0
c1 = 0
jugando = True
salir = False
#le agrego el while y los puntajes
while jugando:

	player = input("\nPlayer, make your move: ").lower()

	if player == "exit":
		jugando = False
		salir = True
	if jugando:
		rand_num = randint(0,2)
		if rand_num == 0:
			computer = "rock"
		elif rand_num == 1:
			computer = "paper"
		else:
			computer = "scissors"

		print(f"\nComputer plays {computer}" )

		if player == computer:
			print("\nIt's a tie!")
		elif player == "rock":
			if computer == "scissors":
				print("\npoint for player!")
				p1 += 1
			else:
				print("\npoint for computer!")
				c1 += 1
		elif player == "paper":
			if computer == "rock":
				print("\npoint for player!")
				p1 += 1
			else:
				print("\npoint for computer!")
				c1 += 1
		elif player == "scissors":
			if computer == "paper":
				print("\npoint for player!")
				p1 += 1
			else:
				print("\npoint for computer!")	
				c1 += 1
		else:
			print("\nPlease enter a valid move!")
		if c1 == 3 or p1 == 3:
			jugando = False
	
if salir:
	print("CAGON! JAJAJAJ")
elif c1 > p1:
	print("\nCOMPUTER WINS")
else:
	print("\nHUMAN WINS")
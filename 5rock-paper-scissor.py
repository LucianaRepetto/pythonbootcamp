print("...rock...")
print("...paper...")
print("...scissors...")
t1 = 0
t2 = 0
#le agrego el for loop y los puntajes

for time in range (5):

    player1 = input("(enter Player 1's choice): ").lower()
    player2 = input("(enter Player 2's choice): ").lower()
    
    print("SHOOT!")

    if player1 == "rock":
        if player2 == "rock":
            print ("empate")
        elif player2 == "paper":
            print("player 2 wins")
            t2 += 1
        else:
            print("player 1 wins")
            t1 += 1

    elif player1 == "paper":
        if player2 == "rock":
            print ("player 1 wins")
            t1 += 1
        elif player2 == "paper":
            print("empate")
        else:
            print("player 2 wins")
            t2 += 1
    else:
        if player2 == "rock":
            print ("player 2 wins")
            t2 += 1
        elif player2 == "paper":
            print("player 1 wins")
            t1 += 1
        else:
            print("empate")     
    if t1 == 3 or t2 == 3:
        break                       


if t1 > t2:
    print("PLAYER 1 MASTER")
else:
    print("PLAYER 2 MASTER")
    
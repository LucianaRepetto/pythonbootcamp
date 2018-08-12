import random

random_number = random.randint(1,10)  # numbers 1 - 10

# handle user guesses
#   if they guess correct, tell them they won
#     otherwise tell them if they are too high or too low

# BONUS - let player play again if they want!


while True:
    usuario = input("Elegi un numero entre 1 y 10: ")
    usuario = int(usuario)    

    if usuario > random_number:
        print("NO, ES MENOR")
    elif usuario < random_number:
        print("NO, ES MAYOR")
    else:
        print("ADIVINASTE!")
        jugar_de_nuevo = input("Querés volver  jugar?(s/n): ")
        if jugar_de_nuevo == "s":
            random_number = random.randint(1,10)
            usuario = None
        else:
            print("Gracias por Jugar!")
            break

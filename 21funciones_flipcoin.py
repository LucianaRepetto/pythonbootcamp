from random import random

def flip_coin():
    r =  random()  #generar un numero random 0-1
    if r > 0.5:
        return "Heads"
    else:
        return "Tails"
print(flip_coin())


#una opcion mas corta
def flip_coin2():

    if random() > 0.5:
        return "Heads"
    else:
        return "Tails"
print(flip_coin2())
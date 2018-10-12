#def print_raiz_cuadrada_de_7():
 #   print(7**2)

# print_raiz_cuadrada_de_7()

def raiz_de_7():
    print("Voy antes que el return!")
    return 7**2
    print("Voy antes que el return!") #nunca lo va a imprimir porque return termina la funcion
result = raiz_de_7()

print(result)

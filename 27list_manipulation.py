'''
la funcion debera tomar 4 parametros (lista, comando, posicion, valor(debe ser opcional))
'''
'''
list_manipulation([1,2,3], "remove", "end") # 3
list_manipulation([1,2,3], "remove", "beginning") #  1
list_manipulation([1,2,3], "add", "beginning", 20) #  [20,1,2,3]
list_manipulation([1,2,3], "add", "end", 30) #  [1,2,3,30]
'''

def list_manipulation(lista, command, position, value= None):
    
    if(command == "remove" and position == "end"):
        return lista.pop()
    elif(command == "remove" and position == "beginning"):
        return lista.pop(0)
    elif(command == "add" and position == "end"):
        lista.append(value)
        return lista
    elif(command == "add" and position == "beginning"):
        lista.insert(0, value)
        return lista
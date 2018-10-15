'''
poner en mayuscula la primera letra de la palabla..
mi prespuesta fue la siguiente
'''
'''
capitalize("tim") # "Tim"
capitalize("matt") # "Matt"
'''

def capitalize(word):
    return word.title()
    
'''
pero otra forma de hacerlo, es con el metodo slice
slice up to index 1 and capitalize it
concatenar y agregarlo al final del primer slice
'''
#def capitalize(string):
 #   return string[:1].upper() + string[1:]
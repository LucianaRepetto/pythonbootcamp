'''
escribir una funcion que tome un parametro (string) y devuelva un diccionario que cada letra tenga
su posicion como valor
'''
'''
multiple_letter_count("awesome") # {'a': 1, 'e': 2, 'm': 1, 'o': 1, 's': 1, 'w': 1}
'''

# flesh out multiple_letter count:
def multiple_letter_count(string):
    return {letter : string.count(letter) for letter in string} 
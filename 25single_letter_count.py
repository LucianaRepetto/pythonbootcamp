'''
funcion que reciba dos parametros, una palabra y una letra. 
hay que contar sin tener en cuenta el case, cuantas veces esta esa letra en esa palara
'''
'''
single_letter_count("Hello World", "h") # 1
single_letter_count("Hello World", "z") # 0
single_letter_count("HelLo World", "l") # 3
'''

#define single_letter_count below:
def single_letter_count(string, letter):
    return string.lower().count(letter.lower())
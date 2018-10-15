'''
una funcion que chequee si el parametro pasado es un palindrome, ya sea una palabra, una oracion, unos numeros, etc
que no tenga en cuenta los espacios en blanco ni el case
'''
'''
is_palindrome('testing') # False
is_palindrome('tacocat') # True
is_palindrome('hannah') # True
is_palindrome('robert') # False
is_palindrome('amanaplanacanalpanama') # True
'''

def is_palindrome(string):
    string.replace(" ", "").lower()
    if string == string[::-1]:
        return True
    return False

'''
una forma refactorizada

def is_palindrome(string):
    string1 = string.replace(" ", "").lower()
    return string1 == string1[::-1]
'''
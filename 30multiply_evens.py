'''
function que multiplique todos los numeros pares 
'''
'''
multiply_even_numbers([2,3,4,5,6]) # 48
'''

def multiply_even_numbers(list):
    prod = 1
    for num in list:
        if num %2 == 0:
          prod = prod * num
    return prod
            
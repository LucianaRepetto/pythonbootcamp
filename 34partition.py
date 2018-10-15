'''
dada una lista de numeros y una callback function q evalua a true o false
si el numero es even o no.
hay que generar dos nuevas listas, una con los valores true y otra con los false
'''
'''
def isEven(num):
    return num % 2 == 0

partition([1,2,3,4], isEven) # [[2,4],[1,3]]
'''

def partition(list2, isEven):
    truthy_list = []
    falsy_list = []
    large_list = [truthy_list, falsy_list]
    
    for n in list2:
        if isEven(n):
            truthy_list.append(n)
        else:
            falsy_list.append(n)
    return large_list
    
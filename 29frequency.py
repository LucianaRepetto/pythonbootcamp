'''
Funcion con dos parametros, el primero una lista y el segundo un termino de busqueda.
ver cuantas veces esta el termino en la lista
'''

'''
frequency([1,2,3,4,4,4], 4) # 3
frequency([True, False, True, True], False) # 1
'''

def frequency(list, search):
    count = 0
    for elem in list:
        if elem == search:
            count +=1
    return count

'''
def frequency(collection, searchTerm):
    return collection.count(searchTerm)
    '''
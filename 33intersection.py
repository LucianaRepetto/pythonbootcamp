'''
devolver solo los valores que coincidan de dos listas pasadas a una funcion
'''

# flesh out intersection pleaseeeee
def intersection(list1, list2):
    return [ n for n in list1 if n in list2]  #esta solucion es con LIST comprehension


'''
pero hay otra manera de resolverlo, con mas pasos
def intersection(l1, l2):
    in_common = []
    for val in l1:
        if val in l2:
            in_common.append(val)
    return in_common
'''
'''
tambien se puede resolver con el método SET(CONVIERTE LAS LISTAS A SET, LO QUE REMUEVE VALORES DUPLICADOS) y se encuentra
los que coinciden con &
def intersection(list1, list2):
    return [val for val in set(list1) & set(list2)]
'''
'''
funcion que tome como argumento una lista, y que solo devuelva los valores verdaderos
'''
'''
compact([0,1,2,"",[], False, {}, None, "All done"]) # [1,2, "All done"]
'''

def compact(list):
    new_list = []
    for thing in list:
        if thing:
            new_list.append(thing)
    return new_list
    
    #return [thing for thing in list if thing]
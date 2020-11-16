

########################################  Diccionarios  ########################################


# Encontrar la suma de números asociados al diccionario #
animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')


def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many individual values are in the dictionary.
    '''
    result = 0    
    for value in aDict.values():
        # Since all the values of aDict are lists, aDict.values() will 
        #  be a list of lists
        result += len(value)
    return result

print(how_many(animals))


# Encontrar la entrada con el valor más largo asociada a ella #

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    result = None
    biggestValue = 0
    for key in aDict.keys():
        if len(aDict[key]) >= biggestValue:
            result = key   # Esto ocurre cuando todo es verdadero en el if #
            biggestValue = len(aDict[key])
    return result
            
    
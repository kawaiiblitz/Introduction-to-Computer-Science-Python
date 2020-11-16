

###################### Tuplas ######################  

# Ej. 1 :  Dada la tupla mostrar el 1er, 3er y 5to elemento en una tupla #
def oddTuples2(aTup):
    '''
    Another way to solve the problem.
 
    aTup: a tuple
     
    returns: tuple, every other element of aTup. 
    '''
    
    #  slicing by 2 to achieve the same result
    return aTup[::2]

oddTuples2(('I', 'am', 'a', 'test', 'tuple'))
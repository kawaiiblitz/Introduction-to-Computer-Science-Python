
################################################ Listas ################################################  


########################### Data Structure ###########################

# Las listas, a diferencia de las tuplas sí son mutables #


listA = [1, 4, 3, 0]
listB = ['x', 'x', 't', 'q']

listA.sort             # Función
listA.sort()           # NoneType
listA.insert(0, 100)   # Inserta al inicio de la lista los números, posición 0.
listA.remove(3)        # Elimina el 3.
listA.append(7)        # Añade el 7 al final de la lista.
listA + listB          # Une las dos listas
listB.sort()           # Ordena alfabéticamente la lista.
listB.pop()            # Elimina el último string de la lista.
listB.count('x')       # Cuenta cuántas x's hay
listB.remove('x')      # Elimina 1 x.
listA.extend([4, 1, 6, 3, 4])    # Añade a la lista esta nueva lista.
listA.count(4)         # Cuenta cuántos 4's hay en la lista.
listA.index(1)         # Nos dice en qué posición se encuentra el 1.
listA.pop(2)           # Elimina de la posición 2 el número 3.
listA.reverse()        # Invierte el sentido de la lista.

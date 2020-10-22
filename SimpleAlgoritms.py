#### Simple Algoritms ####

# 1 #
iteration = 0
count = 0
while iteration < 5:
    # La variable 'letter' en el loop te dice el número de caracteres en la frase, va contándolas
    # en 5 ocasiones 
    for letter in "hello, world": 
        count += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1 
    
    
# 2 #
iteration = 0
while iteration < 5:
    # El count está fuera del for, por lo que al terminar de leer toda la frase se vuelve a
    # restablecer en 0 el contador. 
    count = 0
    for letter in "hello, world":
        count += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1
    
# 3 #
iteration = 0
while iteration < 5:
    count = 0
    for letter in "hello, world":
        count += 1
        # Si la iteración es par, sólo alcanza a leer la primer letra y el contador = 1
        if iteration % 2 == 0:
            break
        # Si es par, el for termina aquí y manda a imprimir, si no es par termina de leer toda 
        # la palabra y manda a imprimir.
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1 
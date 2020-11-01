###################################### Iteración y Recursión ######################################



# Solución Iterativa - Multiplicación #
def mult_iter(a,b):
    result = 0
    while b > 0:
        result += a
        b -= 1     
    return result     # Cuando salga del while manda el resultado #

mult_iter(3,3)




# Factorial por recursión #
def factorial(n):    
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

factorial (4)


# Factorial por iteración #
def factorial_iter(n):
    prod = 1
    
    for i in range (1, n+1):
        prod *= i
    return prod

factorial_iter(4)




# Potencia de un número usando recursión #
def iterPower(base, exp):

    result = 1
    while exp > 0:
        result *= base
        exp -= 1
    return result
    
iterPower(2, 4)


# Potencia de un número usando iteración no x ** x
def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''
    if exp <= 0 :
        return 1
    
    else :
        return base * iterPower(base,exp-1)   
#Una vez completado el ciclo o el if, se va regresando pasos atrás #
    
iterPower(2, 4)




# Torres de Hanoi #

def printMove(fr, to):
    print('move from' + str(fr) + 'to' + str(to))
    
def Towers(n,fr,to,spare):
    if n == 1:
        printMove(fr,to)
    else:
        Towers(n-1, fr, spare, to)
        Towers(1, fr, to, spare)
        Towers(n-1, spare, to, fr)
        
print(Towers(4, 'P1','P2','P3'))



# Máximo Común Divisor iteración #
def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    minimo = min(a,b)
    if a % minimo = 0 and 
        











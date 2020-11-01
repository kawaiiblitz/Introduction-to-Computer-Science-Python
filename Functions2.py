
############### Funciones ################

# Potencia de un número 

x = 9
def square(x) :
    return x ** x

square(x)



# Consecutivo de un número #
# a #
def a(x):
   '''
   x: int or float.
   '''
   return x + 1

a(6)
a(a(6))



# b #
def b(x):
   '''
   x: int or float.
   '''
   return x + 1.0



# c # 
def c(x, y):
   '''
   x: int or float. 
   y: int or float.
   '''
   return x + y



# d #
def d(x, y):
   '''
   x: Can be of any type.
   y: Can be of any type.
   '''
   return x > y

d('apple', 11.1)



# e #
def e(x, y, z):
   '''
   x: Can be of any type.
   y: Can be of any type.
   z: Can be of any type.
   '''
   return x >= y and x <= z

e(a(3), b(4), c(3, 4))



# f #
def f(x, y):
   '''
   x: int or float.
   y: int or float
   '''
   x + y - 2 
   
f


# Otro ejemplo #
x = 12
def g(x):
      x = x + 1
      def h(y):
          return x + y
      return h(6)
g(x)






########################### Método de Objetos #############################

str1 = 'exterminate!' 
str2 = 'number one - the larch'
 
 
str1.upper
str1.upper()  # Out[3]: 'EXTERMINATE!' #
str1
str1.isupper() # Te dice si está en mayúsculas la palabra. Result: False #
str1.islower() # Te dice si está en mayúsculas la palabra. Result: True #
 
str2 = str2.capitalize()
str2    # Cambia la primer letra por mayúscula: 'Number one - the larch' #

str2.swapcase()   # Cambia la primer letra por minúscula y las demás mayúsculas :  'nUMBER ONE - THE LARCH'#

str1.index('e')   # En qué posición se encuentr la letra e, en este caso es en la 0. #

str2.index('n')   # La última posición que se encuentra la n #

str2.find('n')    # La última posición que se encuentra la n #

str2.index('!')   # No lo encuentra #

str2.find('!')    # - 1 significa que no existe #

str1.count('e')   # Cuenta cuántas e's hay en la palabra #

str1 = str1.replace('e', '*')
str1             # Reemplaza las letras e por * :  '*xt*rminat*!' #

str2.replace('one', 'seven')    # Reemplaza donde hay one por seven #






# Fourth Power #
def fourthPower(x):
   '''
   x: int or float.
   '''
   return square(square(x))

x = 4



# Cuando un número sea impar mandar la respuesta True #
def odd(x):
    '''
    x: int
    '''
    return (x % 2 == 1)
odd(9)






















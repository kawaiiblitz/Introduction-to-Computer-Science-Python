# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 21:36:27 2020

@author: Rachel
"""

########## Ciclos ######


""" For  """

"1. Sumar del 7 hasta el 10"

mysum = 0
for i in range (7,10):
    mysum += i #Es lo mismo que x = x + i#
print (mysum)



"2. Sumar del 5 hasta el 11 e irse de dos en dos"

mysum2 = 0
for i in range (5,11,2):
    mysum2 += i #Es lo mismo que x = x + i#
print (mysum2)


" 3. Parar el código anterior cuando se cumpla una condición"
mysum2 = 0
for i in range (5,11,2):
    mysum2 += i #Es lo mismo que x = x + i#
    if mysum2 == 5:
        break
print(mysum2)



""" While  """
n = 0
while n<5:
    print(n)
    n= n + 1
    
    
""" Ejercicio : Write a piece of Python code that prints out the string 'hello world'
 if the value of an integer variable, happy, is strictly greater than 2."""

happy = 3

if happy > 2:    
    print("hello world")
    
    
    
""" Si el comando break se ejecuta dentro de un ciclo, detiene la evaluación del
 ciclo en ese punto y pasa el control a la siguiente expresión.  """  
 
num = 10
while True:
    if num < 7:
        print('Breaking out of loop')
        break
    print(num)
    num -= 1
print('Outside of loop')



num = 100
while not False:
    if num < 0:
        break
print('num is: ' + str(num)) 
    

" While ejercicio 1 "
num = 0
while True:
    num += 2
    print(num)
    if num >= 10:
        print("Goodbye!")
        break
    

" While ejercicio 2 "
num = 11
print("Hello!")
while num > 1:
    num -= 1
    if num %2 == 0:
        print(num)

print("Hello!")
num = 10
while num > 0:
    print(num)
    num -= 2
    
    
" While ejercicio 3 : Si end= 6 sumar 6+5+4+3+2+1 = 21 "    
end = 20
total = 0
current = 1

while current <= end:
    total += current
    current += 1

print(total)


" For ejercicio 1 "
num = 2
for num in range (2,12,2):
    print(num)
    
print ("Goodbye!")



" For ejercicio 2 "
num = 10
print ("Hello!")
for i in range (0,10,2):
    print(num-i)


" For ejercicio 3 "
end = 6
for i in range (1,end):
    end += i 
print (end)   





















    

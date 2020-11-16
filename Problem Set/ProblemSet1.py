###########################################################################################################
######################################### Problem Set 1 ###################################################
###########################################################################################################

s = 'azcbobobegghakl'



# Ejercicio 1 : #
# Contar el número de vocales en la palabra s = 'azcbobobegghakl' #

l =len(s)
count = 0
  
for i in range(l):
    if s[i] == 'a'  or s[i] == 'e' or s[i] == 'i' or s[i] == 'o' or s[i] == 'u':
       count += 1
print('The number of Vowels of s is ' + str(count))
        



# Ejercicio 2 : #
# Contar el número de veces que aparece la secuencia de string 'bob' en la palabra s = 'azcbobobegghakl'#
l =len(s)

bobs = 0
for i in range(l):
    if s[i:i+3] == 'bob':
        bobs += 1
print('Number of times bob occurs is:', bobs)





# Ejercicio 3 : #
# Imprime la cadena más larga de letras ordenadas alfabéticamente de  la palabra s = 'azcbobobegghakl' #
# por ejemplo, "beggh" o si s = 'abcbcd' aparecerá 'abc' #

s = 'azcbobobegghakl'

temp_sub = ""
sub = ""
for i in range(len(s)):
    if s[i] <= s[i+1:len(s)]:
        temp_sub += s[i]
    else:
        temp_sub += s[i]
        if len(temp_sub) > len(sub):
            sub = temp_sub
        temp_sub = ""
print('Longest substring in alphabetical order is: ' + sub )


# Lo que hace por adentro : #
# s[0] < s[0+1:len(s)]
# s[1] < s[1+1:len(s)]
# temp_sub += s[1]

#         if len(temp_sub) > len(sub):
#             sub = temp_sub
#         temp_sub = ""
        

# s[2] < s[2+1:len(s)]
#         temp_sub += s[2]

#         if len(temp_sub) > len(sub):
#             sub = temp_sub
#         temp_sub = ""
        


 
# Otra forma 
# start is the starting index value of the substring
# stop is the ending index value of the substring
# (where it stops being alphabetical)
# we will slice s on these values
# answer holds the substring we will print at the end

s = 'azcbobobegghakl'
start = 0
stop = 0
answer = ''
for ind in range(len(s)):
    # if the index is not the last one
    # and this value is less than the next value
    # then we are alphabetical so set stop to the next value
    if (ind != len(s) - 1) and s[ind] <= s[ind + 1]:
        stop = ind + 1
    # first conditional: if this is the last value in the string
    # or this value is greater than the next value 
    # (meaning we are no longer in alph order) then
    # nested conditional: if the length of this substring is greater
    # than the current answer then save this substring as the answer
    # change the start value to the next index number
    if (ind + 1 == len(s)) or (s[ind] > s[ind + 1]):
        if len(s[start:stop+1]) > len(answer):
            answer = s[start:stop+1]
        start = ind + 1
print('Longest substring in alphabetical order is:', answer) 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "C:/Users/Rachel/Documents/Raquel/Edx/Introduction to Computer Science & Python/Lectura 6. Diccionarios/words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file #
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string #
    line = inFile.readline()
    # wordlist: list of strings #
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program








########### Problem 1 ############ 
secretWord = 'apple' 
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']

def isWordGuessed(secretWord, lettersGuessed):
    '''
    Marca verdadero si adivina la palabra en el conjunto de letterguessed
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    secretWordArray = list(secretWord)
    counter = 0

    for n in range(0,len(secretWord)):
        if secretWordArray[n] in lettersGuessed:
            counter += 1
        else:
            return False

    if counter == len(secretWord):
        return True
    else:
        return False


print(isWordGuessed(secretWord, lettersGuessed))
False









############ Problem 2 ############ 
secretWord = 'apple' 
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    secretWordArray = list(secretWord)
    ahorcado = ""
    
    for n in range(0,len(secretWord)):
        if secretWordArray[n] not in lettersGuessed:
            auxx = '_'            
            
        else:
            auxx = secretWordArray[n] 
        ahorcado += auxx
    return ahorcado

    
print(getGuessedWord(secretWord, lettersGuessed))


# Otra manera #
def getGuessedWord(secretWord, lettersGuessed):
    returningString = ""
    i = 1
    while i <= len(secretWord):
        returningString += "_"
        i += 1

    secretWordArray = list(secretWord)
    returningStringArray = list(returningString)

    for n in range(0,len(secretWord)):
        if secretWordArray[n] in lettersGuessed:
            returningStringArray[n] = secretWordArray[n]
    return ''.join(returningStringArray)

    
print(getGuessedWord(secretWord, lettersGuessed))








############ Problem 3 ############ 

import string
##print(string.ascii_lowercase)    # abcdefghijklmnopqrstuvwxyz
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    lettersGuessed = list(lettersGuessed)
    alfabet = list(string.ascii_lowercase)
    auxx = ""
    d = 0

    
    for n in range(0,len(lettersGuessed)) :
        for i in range(0,len(alfabet)) :
                if lettersGuessed[n] != alfabet[i+d] :
                   auxx += alfabet[i]         
                                      
                else:
                    auxx += ""  
                    d = i 
                n += 1
    return auxx

    
print(getAvailableLetters(lettersGuessed))




#### Otra manera que sí estuvo correcto ###
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']

def getAvailableLetters(lettersGuessed):   
    availableLetters = "abcdefghijklmnopqrstuvwxyz"
    availableLettersArray = list(availableLetters)
    for i in lettersGuessed:   # Para cada uno de los elementos de la lista #
        availableLettersArray.remove(i)

    return "".join(availableLettersArray)     # Convierte una tupla en un string sin separación    
print(getAvailableLetters(lettersGuessed))

    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...






# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)

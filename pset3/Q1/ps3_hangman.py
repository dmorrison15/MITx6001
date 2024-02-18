# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
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
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    return all(letter in lettersGuessed for letter in secretWord)


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    result = ''
    for letter in secretWord :
      if letter not in lettersGuessed :
        result += '_'
      else :
        result += letter
    return result


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    allLetters = 'abcdefghijklmnopqrstuvwxyz'
    unusedLetters = ''
    for letter in allLetters :
      if letter not in lettersGuessed :
        unusedLetters += letter
    return unusedLetters
  

def welcomePlayer(secretWord) :

  # prints a welcome message to the player and tells them the length of the secret word
  numLetters = len(secretWord)
  print("Welcome to the game Hangman!")
  if numLetters == 1 :
    print("I am thinking of a word that is", numLetters, "letter long.")
  else :
    print("I am thinking of a word that is", numLetters, "letters long.")
    
def buffer() :
  print(12*'_')


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
    welcomePlayer(secretWord)
    
    guessesLeft = 8
    lettersGuessed = []

    while guessesLeft > 0 :
      
      buffer()
      
      #tell player how many guesses they have and the letters they haven't guessed yet
      print('You have', guessesLeft, 'guesses left.')
      print('Available letters:', getAvailableLetters(lettersGuessed))
      
      guess = input('Please guess a letter: ')
      #if the player guesses the same letter twice, they are told and the round is reset
      if guess in lettersGuessed :
        print("Oops! You've already guessed that letter:", getGuessedWord(secretWord, lettersGuessed))
        continue
        
      lettersGuessed += guess
      
      #if the guess is correct, the secret word is updated to reveal the letter
      if guess in secretWord :
        print("Good guess:", getGuessedWord(secretWord, lettersGuessed))
      
      #if the guess is wrong, the player loses a guess 
      else :
        print("Oops! That letter is not in my word:", getGuessedWord(secretWord, lettersGuessed))
        guessesLeft -= 1
      
      #Congratulate player if they guess the secret word
      if isWordGuessed(secretWord, lettersGuessed) :
        print("Congratulations, you won!")
        break
    
  #Reveal the secret word if the player loses    
    if isWordGuessed(secretWord, lettersGuessed) == False :
      print("Sorry, you ran out of guesses. The word was", secretWord)
      
       
      
    




# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
secretWord = "apples"
hangman(secretWord)

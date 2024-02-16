#returns a string of the letters that haven't been guessed by the user
def getAvailableLetters(lettersGuessed) :
  allLetters = 'abcdefghijklmnopqrstuvwxyz'
  unusedLetters = ''
  for letter in allLetters :
    if letter not in lettersGuessed :
      unusedLetters += letter
  return unusedLetters

#returns a string of the secret word with a '_' in the place of an unguessed letter
def getGuessedWord(secretWord, lettersGuessed) :
  result = ''
  for letter in secretWord :
    if letter not in lettersGuessed :
      result += '_'
    else :
      result += letter
  return result

#returns boolean of whether or not all letters in the secret word have been guessed
def isWordGuessed(secretWord, lettersGuessed) :
  return all(letter in lettersGuessed for letter in secretWord)

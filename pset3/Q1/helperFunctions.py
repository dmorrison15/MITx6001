def getAvailableLetters(lettersGuessed) :
  allLetters = 'abcdefghijklmnopqrstuvwxyz'
  unusedLetters = ''
  for letter in allLetters :
    if letter not in lettersGuessed :
      unusedLetters += letter
  return unusedLetters

def getGuessedWord(secretWord, lettersGuessed) :
  result = ''
  for letter in secretWord :
    if letter not in lettersGuessed :
      result += '_'
    else :
      result += letter
  return result

def isWordGuessed(secretWord, lettersGuessed) :
  for letter in secretWord :
    if letter not in lettersGuessed :
      return False
  return True

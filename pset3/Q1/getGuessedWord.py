def getGuessedWord(secretWord, lettersGuessed) :
  result = ''
  for letter in secretWord :
    if letter not in lettersGuessed :
      result += '_'
    else :
      result += letter
  return result

secretWord = 'apple'
lettersGuessed = ['e', 'i', 'k', 'p', 'r']
print(getGuessedWord(secretWord, lettersGuessed))
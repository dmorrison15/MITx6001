def getAvailableLetters(lettersGuessed) :
  allLetters = 'abcdefghijklmnopqrstuvwxyz'
  unusedLetters = ''
  for letter in allLetters :
    if letter not in lettersGuessed :
      unusedLetters += letter
  return unusedLetters

lettersGuessed = ['e', 'r', 't', 's', 'x']
print(getAvailableLetters(lettersGuessed))

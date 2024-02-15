def isWordGuessed(secretWord, lettersGuessed) :
  for letter in secretWord :
    if letter not in lettersGuessed :
      return False
  return True


secretWord = 'apple'
lettersGuessed = ['e', 'i', 'l', 'p', 'r', 'a']
print(isWordGuessed(secretWord, lettersGuessed))
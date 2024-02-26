def keysWithValue(aDict, target) :
  targetKeys = []
  for key in aDict :
    if aDict[key] == target :
      targetKeys += {key : target}
  targetKeys.sort()
  return targetKeys

aDict = {4 : 5, 6 : 4, 2 : 5, 1 : 5}
print(keysWithValue(aDict, 5))
      
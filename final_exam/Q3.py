def uniqueValues(aDict):
  '''
  aDict: a dictionary
  returns: a sorted list of keys that map to unique aDict values, empty list if none
  '''
  uniqueKeys = []
  vals = list(aDict.values())
  for key in aDict:
    if vals.count(aDict[key]) == 1:
      uniqueKeys.append(key)
  uniqueKeys.sort()
  return uniqueKeys

print(uniqueValues({1:3, 2:4, 3:3, 4:6, 5:2, 6:4}))
print(uniqueValues({1:3, 2:4, 3:3, 4:6, 5:6, 6:4}))

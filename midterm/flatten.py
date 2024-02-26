def flatten(aList) :
  flatList = []
  for thing in aList :
    if isinstance(thing, int) or isinstance(thing, str) :
      flatList.append(thing)
    else :
      flatten(thing)
    return flatList
aList = [[1, 2, 3], 4, 5, 6, 'a', ['b','c']]
print(flatten(aList))
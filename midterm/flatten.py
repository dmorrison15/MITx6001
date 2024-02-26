def flatten(aList) :
  flatList = []
  for thing in aList : 
    try: 
      flatList.extend(flatten(thing))
    except :
      flatList.append(thing)
  return flatList
    
aList = [[1,[2], 3], 4, 5, 6, 'a', ['b','c']]
print(flatten(aList))
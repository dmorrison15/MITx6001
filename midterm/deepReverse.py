def deep_reverse(L) :
  L.reverse()
  for i in L :
    i.reverse()
list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
deep_reverse(list)
print(list)
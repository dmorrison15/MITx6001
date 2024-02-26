def f(s) :
  return 'a' in s
def satisfiesF(L) :
  for i in L :
    if not f(i) :
      L.remove(i)
  return len(L)

L = ['a', 'b', 'a']
print(satisfiesF(L))
print(L)
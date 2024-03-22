def largest_odd_times(L):
  """ Assumes L is a non-empty list of ints
      Returns the largest element of L that occurs an odd            number 
      of times in L. If no such element exists, returns None """
  largest_odd_elem = None
  for i in L:
    i_count = L.count(i)
    if i_count % 2 == 1 and i > int(0 if largest_odd_elem is None else largest_odd_elem):
        largest_odd_elem = i
  return largest_odd_elem

print(largest_odd_times([1, 2, 1, 2]))
print(largest_odd_times([1, 1, 2, 3, 3, 1]))
print(largest_odd_times([1, 1, 1, 2]))
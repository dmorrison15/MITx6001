def sum_digits(s):
  """ assumes s a string
      Returns an int that is the sum of all of the digits in s.
        If there are no digits in s it raises a ValueError exception. """
  # Your code here
  num_count = 0
  total = 0
  for i in s:
    try:
      total += int(i)
      num_count += 1
    except ValueError:
      continue
  if num_count == 0:
    raise ValueError('string must include integer')    
  return total

print(sum_digits('hello'))
print(sum_digits('abc123'))
print(sum_digits('12345'))
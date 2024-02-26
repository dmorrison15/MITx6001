def closest_power(base, num) :
  pow = 0
  closest_pow = 0
  lowest_diff = num - 1
  while True :
    ans = base ** pow
    cur_diff = abs(num - ans)
    if cur_diff < lowest_diff :
      lowest_diff = cur_diff
      closest_pow = pow
    if ans > num :
      break
    pow += 1
  return closest_pow
print(closest_power(4, 1))
    
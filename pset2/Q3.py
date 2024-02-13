# CONSTANTS
balance = 320000
annualInterestRate = 0.20

# The upper and lower bounds are the boundaries in which the answer will be searched for. The upper and lower bounds are each initialized with their highest or lowest possible values. 
upperBound = (balance + balance * annualInterestRate) / 12
lowerBound = balance / 12

monthlyInterestRate = annualInterestRate / 12

# This infinite while loop uses bisection search to find the monthly payment so long as the current balance is within a few of 0.
while True :
  monthlyPayment = round((upperBound + lowerBound) / 2, 2)
  curBalance = balance
  for i in range(12) :
    unpaid_balance = curBalance - monthlyPayment
    curBalance = round((unpaid_balance + monthlyInterestRate * unpaid_balance), 2)
  if abs(curBalance) < 0.15 :
    break
  if curBalance > 0 :
    lowerBound = monthlyPayment
  elif curBalance < 0 :
    upperBound = monthlyPayment
  # The monthly payment has a margin of error of about 1 cent
print('Lowest Payment:', monthlyPayment)

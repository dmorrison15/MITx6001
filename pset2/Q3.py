# Constants
balance = 999999
annualInterestRate = 0.18

upperBound = (balance + balance * annualInterestRate) / 12
lowerBound = balance / 12
monthlyInterestRate = annualInterestRate / 12

# This infinite while loop uses bisection search to find the monthly payment so long as the current balance after a year is not 0
while True :
  monthlyPayment = round((upperBound + lowerBound) / 2, 2)
  print(monthlyPayment)
  curBalance = balance
  for i in range(12) :
    unpaid_balance = curBalance - monthlyPayment
    curBalance = round((unpaid_balance + monthlyInterestRate * unpaid_balance), 2)
  if curBalance > 0 :
    lowerBound = monthlyPayment
  elif curBalance < 0 :
    upperBound = monthlyPayment    
  else :
    break
print('Lowest Payment:', monthlyPayment)
# 29157.09
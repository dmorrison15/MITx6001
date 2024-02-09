balance = int(input('balance: '))
curBalance = 0
annualInterestRate = float(input('annual interest rate: '))
monthlyPayment = 10
monthlyInterestRate = annualInterestRate / 12
while True:
  for i in range(12) :
    unpaid_balance = balance - monthlyPayment
    curBalance = round(unpaid_balance + (monthlyInterestRate * unpaid_balance),  12)
  if curBalance >= balance :
    break
  monthlyPayment += 10
print('Lowest Payment:', monthlyPayment)
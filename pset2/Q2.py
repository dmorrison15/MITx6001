balance = int(input('balance: '))
curBalance = balance
annualInterestRate = float(input('annual interest rate: '))
monthlyInterestRate = annualInterestRate / 12
monthlyPayment = 10
while True:
  for i in range(12) :
    unpaid_balance = curBalance - monthlyPayment
    curBalance = round(unpaid_balance + (monthlyInterestRate * unpaid_balance),  2)
  if curBalance <= balance :
    break
  monthlyPayment += 10
print('Lowest Payment:', monthlyPayment)
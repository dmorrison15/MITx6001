# CONSTANTS
balance = 3329
annualInterestRate = 0.2
monthlyInterestRate = annualInterestRate / 12

# Logic
monthlyPayment = 10
# infinite loop that will keep increasing monthly payment by 10 so long as balance isn't paid off
while True:
  #reset current balance to initial balance
  curBalance = balance
  # determine unpaid balance each month
  for i in range(12) :
    unpaid_balance = curBalance - monthlyPayment
    curBalance = round(unpaid_balance + (monthlyInterestRate * unpaid_balance),  2)
  
  # if current balance is fully paid off then break out of infinite loop  
  if curBalance <= 0 :
    break
  monthlyPayment += 10
print('Lowest Payment:', monthlyPayment)
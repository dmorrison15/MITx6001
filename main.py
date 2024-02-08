balance = int(input('Give a balance amount: '))
annual_interest_rate = float(input('Give an interst rate: '))
monthly_payment_rate = float(input('Give a monthly payment rate: '))
print('')

monthly_interest_rate = annual_interest_rate / 12

for i in range(12) :
  monthly_payment = monthly_payment_rate * balance
  unpaid_balance = balance - monthly_payment
  balance = round(unpaid_balance + (monthly_interest_rate * unpaid_balance), 2) 


print('Remaining balance:', str(balance))

#Comment
balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
month = 0
updated_balance = balance
while month < 12:
    monthly_interest_rate = annualInterestRate / 12.0
    minimum_payment = updated_balance * monthlyPaymentRate
    updated_balance -= minimum_payment
    updated_balance = updated_balance + (updated_balance * monthly_interest_rate)
    month += 1
print(updated_balance)
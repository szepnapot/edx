# Monthly interest rate = (Annual interest rate) / 12.0
# Monthly unpaid balance = (Previous balance) - (Minimum fixed monthly payment)
# Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)

balance = 4773
annualInterestRate = 0.2
monthly_interest_rate = annualInterestRate / 12.0
monthly_payment = 10

def getBalanceByEndOfYear(balance, monthly_payment, monthly_interest_rate, month=1):
    if month > 12:
        return round(balance, 2)
    else:
        balance -= monthly_payment
        updated_balance = balance + (balance * monthly_interest_rate)
        return getBalanceByEndOfYear(updated_balance, monthly_payment, monthly_interest_rate, month + 1)

balance_by_end = getBalanceByEndOfYear(balance, monthly_payment, monthly_interest_rate)

while balance_by_end > 0:
    monthly_payment += 10
    balance_by_end = getBalanceByEndOfYear(balance, monthly_payment, monthly_interest_rate)


print(monthly_payment)




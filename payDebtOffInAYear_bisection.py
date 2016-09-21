balance = 320000
annualInterestRate = 0.2
monthly_interest_rate = annualInterestRate / 12.0

def getBalanceByEndOfYear(balance, fixed_monthly_payment, month=1):
    if month > 12:
        return round(balance, 2)
    else:
        balance -= fixed_monthly_payment
        updated_balance = balance + (balance * monthly_interest_rate)
        return getBalanceByEndOfYear(updated_balance, fixed_monthly_payment, month + 1)

lower_bound = balance / 12
upper_bound = (balance * (1 + monthly_interest_rate)**12) / 12.0

while True:
    guess = (lower_bound + upper_bound) / 2
    balanceByEndOfYear = getBalanceByEndOfYear(balance, guess)
    if balanceByEndOfYear == 0:
        break
    elif balanceByEndOfYear > 0:
        lower_bound = (guess + lower_bound) / 2
    else:
        upper_bound = guess


print(round(guess, 2))
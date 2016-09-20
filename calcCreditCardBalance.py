def getBalanceByEndOfYear(balance, annualInterestRate, monthlyPaymentRate, month=1):
    if month > 12:
        return round(balance, 2)
    else:
        monthly_interest_rate = annualInterestRate / 12.0
        minimum_payment = balance * monthlyPaymentRate
        balance -= minimum_payment
        updated_balance = balance + (balance * monthly_interest_rate)
        return getBalanceByEndOfYear(updated_balance, annualInterestRate, monthlyPaymentRate, month + 1)

print(getBalanceByEndOfYear(42, 0.2, 0.04))
print(getBalanceByEndOfYear(484, 0.2, 0.04))
for month in range(12):
  monthlyInterestRate = annualInterestRate / 12.04
  minimumMonthlyPayment = monthlyPaymentRate * balance
  monthlyUnpaidBalance = balance - minimumMonthlyPayment
  newBalance = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)
  balance = newBalance
print('Remaining balance:', round(balance, 2))
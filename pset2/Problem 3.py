epsilon = 1
monthlyInterestRate = annualInterestRate / 12.0
newBalance = balance
low = balance / 12
high = (balance * (1 + monthlyInterestRate) ** 12) / 12.0
  
while abs(newBalance - epsilon) > 1:
  minimumMonthlyPayment = (low + high) / 2
  for month in range(12):
    monthlyUnpaidBalance = newBalance - minimumMonthlyPayment
    newBalance = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)
    
  if newBalance > -epsilon and newBalance < epsilon:
    print('Lowest Payment:', round(minimumMonthlyPayment, 2))
    break
  if newBalance < -epsilon:
    high = minimumMonthlyPayment
  elif newBalance > epsilon:
    low = minimumMonthlyPayment
  newBalance = balance
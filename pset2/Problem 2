newBalance = balance
minimumMonthlyPayment = 10
monthlyInterestRate = annualInterestRate / 12.0
  
while newBalance > 0:
  for month in range(12):
    monthlyUnpaidBalance = newBalance - minimumMonthlyPayment
    newBalance = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)
      
  if newBalance <= 0 or monthlyUnpaidBalance <= 0:
    break
    
  newBalance = balance
  minimumMonthlyPayment += 10
    
print('Lowest Payment:', minimumMonthlyPayment)
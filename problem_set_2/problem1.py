balance = 42
annualInterestRate  = 0.2
monthlyPaymentRate  = 0.04

print_txt = 'Month {month} Remaining balance: {balance}'
#https://www.w3schools.com/python/ref_string_format.asp
#https://www.w3schools.com/python/ref_func_round.asp

for i in range(12):
    up = balance * (1 - monthlyPaymentRate )
    balance = (1 + annualInterestRate/12) * up
    
    print(print_txt.format(month=i,balance=round(balance,2)))


print('Remaining balance: ' + str(round(balance,2)))



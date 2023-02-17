balance = 4773
annualInterestRate  = 0.2

check_balance = balance
fixedMonthlyPayment  = 10

while check_balance >= 0:
    for i in range(12):
        up = check_balance - fixedMonthlyPayment
        check_balance = (1 + annualInterestRate/12) * up
        
        #print(print_txt.format(month=i,balance=round(balance,2)))
    
    if (check_balance < 0) :
        break
    else :
        check_balance = balance
        fixedMonthlyPayment += 10

print('Lowest Payment: ',fixedMonthlyPayment)          



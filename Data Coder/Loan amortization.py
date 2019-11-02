principal_amount = int(input ("Enter Principal Amount: "))
interest_annual = int(input ("Enter Annual Interest Rate: "))
period_years = int(input ("Enter duration of loan in years: "))
period = period_years *12
interest_rate = (interest_annual) / (100*12)

# Amortization amount = P(i*[(1+i)p])
#                       --------------
#                         [(1+i)p]-1
def calculate_amortization_amount (principal_amount, interest_rate, period):
    x = (1 + interest_rate) ** period
    return principal_amount * (interest_rate * x) / (x - 1)

def amortization_schedule (principal_amount, interest_rate, period):
    amortization_amount = calculate_amortization_amount(principal_amount, interest_rate, period)
    month = 1
    print ('Month'.center(20),'!', 'Principal'.center(20),'!', 'Interest Payment'.center(20),'!', 'Principal Payment'.center(20),'!', 'Ending Principal'.center(20))
    print ('-------------------'.center(20),'!', '-------------------'.center(20),'!','-------------------'.center(20),'!','-------------------'.center(20),'!','-------------------'.center(20),'!','-------------------'.center(20),)
    while month<= period:
        interest_payment = interest_rate * principal_amount
        principal_payment = amortization_amount - interest_payment
        ending_principal = principal_amount - principal_payment
        print (str(month).center(20),'!', str(round(principal_amount,3)).center(20),'!', str(round(interest_payment,3)).center(20),'!', str(round(principal_payment,3)).center(20),'!', str(round(ending_principal,3)).center(20))
        month = month + 1
        principal_amount = ending_principal

amortization_schedule (principal_amount,interest_rate,period)

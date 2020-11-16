
############################## Problem Set 2 ##############################



# Problema 1 #

balance = 100
annualInterestRate = 0.04
monthlyPaymentRate = 0.02   

def remaning_balance(balance,annualInterestRate,monthlyPaymentRate) :
    balance = balance
    mes = 1
    while mes < 13 :         
        Monthly_interest_rate = annualInterestRate / 12.0
        Minimum_monthly_payment = monthlyPaymentRate * balance
        balance = balance - Minimum_monthly_payment
        balance = round(balance + (Monthly_interest_rate * balance),2)
        mes += 1
        
    print('Remaining balance:' + str(balance) )    
    return(balance)
   
remaning_balance(balance,annualInterestRate,monthlyPaymentRate)



# Problema 2 #

balance = 4226
annualInterestRate = 0.04

lowestPayment = 200
initialBalance = balance
while balance > 0:
    # iterate over 12 months
    for i in range(12):
        unpaidBalance = balance - lowestPayment
        interest = unpaidBalance * (annualInterestRate / 12.0)
        # update the balance
        balance = unpaidBalance + interest   
    if balance < 0:   # Cuando termina el ciclo entonces ya se va a las condiciones #
        print("Lowest Payment:",lowestPayment)
    else:
        # reset the balance to it's initial value
        balance = initialBalance
        lowestPayment += 10
        
        

# Problema 3 #
balance = 320000
annualInterestRate = 0.2

initialBalance = balance

paymentLowerBound = balance / 12
paymentUpperBound = (balance * (1 + (annualInterestRate / 12.0))**12) / 12.0
guessPayment = (paymentLowerBound + paymentUpperBound) / 2
epsilon = 0.01

while balance >= epsilon:
    # iterate over 12 months
    for i in range(12):
        unpaidBalance = balance - guessPayment
        interest = unpaidBalance * (annualInterestRate / 12.0)
        # update the balance
        balance = unpaidBalance + interest

    if abs(balance) < epsilon:
        print("Lowest Payment",round(guessPayment,2))
        # break out of the loop
        break
    elif balance < 0:
        paymentUpperBound = guessPayment
    else:
        paymentLowerBound = guessPayment

    guessPayment = (paymentLowerBound + paymentUpperBound) / 2
    # reset the balance to it's initial value
    balance = initialBalance




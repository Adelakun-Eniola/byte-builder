'''
ask user to input the amount he wants  to borrow and store as principal
prompt user to input the annual interest rate  store as annual_interest_rate
 prompt user to input how long he wants  to borrow and store as durattion
  
'''


principal = float(input("Enter Amount You Wish To Borrow:"))
#print("$", principal)

annual_interest_rate = float(input("Enter AnnualInterest Rate: "))


monthly_interest_rate = annual_interest_rate/(100*12)


duration = float(input("Enter Duration In Years:"))
#print(duration)


number_of_months = duration *12


numerator = principal* (monthly_interest_rate*(1 + monthly_interest_rate)** number_of_months / (((1 + monthly_interest_rate)** number_of_months )-1))
#denominator = (1 + monthly_interest_rate)** number_of_months -1


print ("Yout Monthly Payment is $", round(numerator, 2))



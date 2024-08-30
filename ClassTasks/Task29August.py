"""ask the user hoe much he wants to deposit and store as deposit
ask the user how nuch he wants to withdraw store as withdraw

"""

def depositfunction():
    deposit = int(input("How Much You Wanna Deposit: "))

depositfunction()
def maincalculation():
    
    print("Do You wish to deposit again: ")
    inputs = """
        1. Yes
        2. No
        """
    print(inputs)
    input_one = int(input("Choose: "))
    while(input_one == 1):
        depositfunction()
    if input_one ==2:
        print("Okay")

maincalculation()

withdraw = int(input("How much you wan withdraw: "))

#account_balance = deposit - withdraw
#print("Your Account Balance is: ", account_balance)

    






'''
count = 0
while (1<=umberof deposits):
'''
                
            

    
   



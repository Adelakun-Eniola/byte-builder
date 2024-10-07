'''import random
passed = 0
failed = 0

for index in range(1,11):
    number_one = random.randrange(10)
    print(number_one)
    number_two = random.randrange(10)
    print(number_two)
    
    if number_one < number_two:
        while number_one < number_two:
            print("PLEASE KINDLY IGNORE THE FIRST TWO NUMBERS THANKS!!")
            break
        else:
            continue
        number_one = random.randrange(10)
        print(number_one)
        number_two = random.randrange(10)
        print(number_two)
    
    total = number_one - number_two
    user = int(input("Subtract these values and print the answer please??: "))
    if user != total:
        print("incorrect")
        failed+=1
    else:
        print("correct")
        passed+=1
print("Passed: ", passed)
print("Failed: ", failed)




 first_level = user_taxable_income - 8350
            tax_one = (10/100) * first_level
'''

#filing statuses:
#married jointly
#married separately
#hoh
#singles
# first cut is at 83.5%

user_taxable_income = float(input("Enter Income: "))

filings = """
    0. Single Filers
    1. Married Filing jointly
    2. Married Filing Separately
    3. Head Of HouseHold
    
"""
print(filings)
user_filings = int(input("Choose A filing number please: "))

match user_filings:
   
    
    case 0:
        if user_taxable_income > 0 and user_taxable_income < 8350:
            
            tax_one = (0.1) * user_taxable_income
            print(tax_one)
        elif user_taxable_income > 8351 and user_taxable_income < 33950:
            tax_one = (0.1) * user_taxable_income
            subtract = user_taxable_income - 8350
            tax_two = (0.15) * subtract
            print(tax_one + tax_two)
        elif user_taxable_income > 33951 and user_taxable_income < 82250:
            tax_one = (0.1) * user_taxable_income
            subtract = user_taxable_income - 8350
            subtract2 = subtract - 33950
            tax_two = (0.15) * subtract
            tax_three = (0.25) * subtract2
            print(tax_one + tax_two + tax_three)
        elif user_taxable_income > 82251 and user_taxable_income < 171550:
            tax_one = (0.1) * user_taxable_income
            subtract = user_taxable_income - 8350
            subtract2 = subtract - 33950
            subtract3 = subtract2 - 82250
            tax_two = (0.15) * subtract
            tax_three = (0.25) * subtract2
            tax_four = (0.28) * subtract3
            print(tax_one + tax_two + tax_three + tax_four)
        elif user_taxable_income > 171551 and user_taxable_income < 372950:
            tax_one = (0.1) * user_taxable_income
            subtract = user_taxable_income - 8350
            subtract2 = subtract - 33950
            subtract3 = subtract2 - 82250
            subtract4 = subtract3 - 171550
            tax_two = (0.15) * subtract
            tax_three = (0.25) * subtract2
            tax_four = (0.28) * subtract3
            tax_five = (0.33) * subtract4
            print(tax_one + tax_two + tax_three + tax_four + tax_five)
        elif user_taxable_income > 372951:
            tax_one = (0.1) * user_taxable_income
            subtract = user_taxable_income - 8350
            subtract2 = subtract - 33950
            subtract3 = subtract2 - 82250
            subtract4 = subtract3 - 171550
            subtract5 = subtract4 - 372950
            tax_two = (0.15) * subtract
            tax_three = (0.25) * subtract2
            tax_four = (0.28) * subtract3
            tax_five = (0.33) * subtract4
            tax_six = (0.35)* subtract5
            print(tax_one + tax_two + tax_three + tax_four + tax_five+ tax_six)

        
            
            
            
            
            
        
            
            
        

import random
'''user_principal = int(input("Enter principal: "))
user_year = int(input("Enter year: "))
user_rate = int(input("Enter rate : "))

for i in range(1, user_year + 1):
    roi = user_principal * (user_rate / 100)
    new_principal = user_principal + roi
    print(f"{i} {roi:,.2f} {new_principal:,.2f}")
    user_principal = new_principal
    

#15,45,30

for number in range(1,51):
    if number%3 ==0 and number %5 == 0:
        print("fizzbuzz")
    elif number % 3 == 0:
        print("fizz")
    elif number % 5 ==0:
        print ("buzz")
    else:
        print(number, end = " ")

'''
number_one = random.randrange(10,100)
number_two = random.randrange(10,100)
number_three = random.randrange(10,100)

print(f'{[number_one]}')
print(f'{[number_two]}')
print(f'{[number_three]}')
user = input('Enter Three Double digit number : '). split()

xtract1 = user % 100
number1 = user // 100

xtract2 = number1 % 100
number2 = number1 // 100

print(xtract1, xtract2, number2)

if number_one == xtract1 and number_two == xtract2 and number_three == number2:
    print("You Won $4k")
else:
    print("FAiled")





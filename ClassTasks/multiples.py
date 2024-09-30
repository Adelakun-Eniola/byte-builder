'''n = 0
for number in range(1, 20000):
    if number %10 == 0:
        n = n + number
print(n)
        

        
for line in range(3, 48, 3):
    print(line, end = " ",)
    
for even in range(1, 100):
    if even% 2 == 0:
        print(even, end = " ")




for eniola in range(5, 0, -1):
    for number2 in range(eniola,0, -1):
        print(number2, end = " ")
    print()
    


user = int(input("Enter A Number: "))
rows = user
for i in range(1, user, ):
    for j in range(1, j<=i, j = j+1):
        print('*')
    print()
    


user_input = int(input('Sample output: '))
for number in range(1, 11):
    print (user_input ,'*', number ,'=', user_input * number)


def getmaximum(number_one, number_two, number_three):
    if number_one > number_two and number_one > number_three:
        return number_one
    elif number_two > number_one and number_two > number_three:
        return number_two
    else:
        return number_three
print(getmaximum(7,9,3))
'''

def getminimum(number_one, number_two, number_three):
    if number_one < number_two and number_one < number_three:
        return number_one
    elif number_two < number_one and number_two < number_three:
        return number_two
    else:
        return number_three
print(getminimum(7,9,3))

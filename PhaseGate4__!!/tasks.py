'''
rows = 5
for index in range(1, rows+1):
    for number in range(1, index+1):
        if number % 2 == 0:
            print("*", end = " ")
        else:
            print(number, end = " ")
    print()




rows = 7
for index in range(1, rows+1):
    for number in range(1, index+1):
        if number % 2 == 0:
            print("*", end = " ")
        else:
            print(number, end = " ")
    print()
for index in range(1, rows+1):
    for number in range(1, rows-index):
        if number %2 == 0:
            print("*", end = " ")
        else:
            print(number, end = " ")
    print()

number = 500
total = 1
counter =0
for i in range(number, ):
    counter+=1
    total+=counter
    if total <= number:
        print(total -2, end=" ")


def factorial(number):
    product =1
    for i in range(number):
        factorial = number -i
        #print(factorial)
        product = product * factorial
    print(product)
factorial(12)
'''
number = 7
first_number =0
second_number = 0
third_number = 1
count = 0
for i in range(number):
    first_number = second_number
    second_number = third_number
    third_number = first_number+second_number
    count+=1
    print(third_number, end = " ")

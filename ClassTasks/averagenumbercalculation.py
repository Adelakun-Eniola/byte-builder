'''
ask the user to enter a number
store the number as number_one
ask the user to enter a second number
store the second number as number_two
ask user to enter number three
store the third number as number_three

add the three numbers together
store the result as total_answer
divide the total_answer by 3
store answer as average 
print average
'''

number_one = int(input("Enter A Number: "))
number_two = int(input("Enter A Second  Number: "))
number_three = int(input("Enter Third Number: "))

total_answer = number_one + number_two + number_three

average = total_answer/3
print("The average of the number is " , round(average, 4))
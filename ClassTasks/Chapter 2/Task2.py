user_input = int(input("Enter five digits: "))
first_digit = user_input % 10
#print(first_digit)
firstfloordivision = user_input // 10
#print(firstfloordivision)
second_digit = firstfloordivision % 10
#print(second_digit)

second_floordivision = firstfloordivision // 10
#print(second_floordivision)

third_digit = second_floordivision%10
#print(third_digit)


third_floordivision = second_floordivision //10
forth_digit = third_floordivision % 10

fourth_floordivision = third_floordivision // 10
fifth_digit = fourth_floordivision % 10

 
print(fifth_digit,forth_digit,third_digit,second_digit,first_digit)

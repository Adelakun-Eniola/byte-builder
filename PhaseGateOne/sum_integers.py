user_input = int(input("Enter A Number Between 0 To 1000:   "))
xtract_one = user_input % 10
new_value = user_input //10
xtract_two = new_value %10
new_value_two = new_value //10


total = xtract_one + xtract_two + new_value_two
print(total)

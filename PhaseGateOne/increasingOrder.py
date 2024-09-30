input_one = int(input("Enter First NUmber: "))
input_two = int(input("Enter First NUmber: "))
input_three= int(input("Enter First NUmber: "))

total = input_one + input_two + input_three
lowest = input_one

if input_two < input_one:
    lowest = input_one
if input_three < input_one:
    lowest = input_three

highest = input_one
if input_two > input_one:
    highest = input_two
if input_three > input_one:
    highest = input_three

mid = total - lowest - highest

print(lowest, mid, highest)



user_input = int(input("Enter Number: "))
if user_input == "A-Z":
    print("Invalid Syntax")
for number in range(1, 11):
    used = user_input* number
    print(user_input, "x", number ,'=', used)



'''
counter = 1
while (counter <=10):
    table = user_input * counter
    print( table)
    counter +=1
'''

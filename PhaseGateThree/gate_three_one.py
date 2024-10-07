'''a = 9
if a >5 and a<=10:
    print("hello")
else:
    print("bye")
'''
'''
user_input = int(input("ENter A Number: "))
if user_input % 7 ==0:
    print(True)
else:
    print(False)

if user_input % 3 ==0:
    print(True)
else:
    print(False)
'''
'''
number = 345678
xtract = number % 10
print(xtract)
'''
'''
user = int(input('Enter cost Of your car: '))
if user > 0 and user <=  2500000:
    dutycharge = (5/100)* user
    print("Your duty charge percentage is 5% and duty charge is ", dutycharge)
elif user > 2500000 and user <= 5000000:
    dutycharge2 = (10/100)* user
    print("Your duty charge percentage is 10% and duty charge is ", dutycharge2)
elif user > 5000000 and user <=  10000000:
    dutycharge3 = (15/100)* user
    print("Your duty charge percentage is 15% and duty charge is ", dutycharge3)
elif user >=  10000000:
    dutycharge4 = (20/100)* user
    print("Your duty charge percentage is 20% and duty charge is ", dutycharge4)
else:
    print("No loan Please")
'''
daysoftheweek = """
    1 = Monday
    2 = Tuesday
    3 = Wednesday
    4 = Thursday
    5 = Friday
    6 = Saturday
    7 = Sunday
"""
user = int(input('Enter A Number From 1 to 7: '))
while user > 7 and user< 0:
    print("No valid input")
    user = int(input('Enter A Number From 1 to 7: '))
match user:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")

'''
#A > B and C > D

'''
#as unit increases price also increases
#that means for every 100 unit the price increases by #50
#now 


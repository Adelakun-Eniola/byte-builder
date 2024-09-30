import random

for number in range(0,1):
    number1 = (random.randrange(1,100))
    number2 = (random.randrange(1,100))
    print(number1, number2)
    total = number1+number2

user = int(input("Ente The Sum Of The Two Numbers:"))
if user == total:
    print("true")
else:
    print("false")



#print(total)
   

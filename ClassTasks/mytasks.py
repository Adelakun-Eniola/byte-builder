'''user = 5
for number in range(1, user+1):
    for num in range(1, number+1):
        print(num, end = ' ')
    print(' ')


#collect number from user, run till user wants to stop, add to list



sumtotal = 0
counter = 0
totalIndex = []
while True:
    user_input2 = int(input("ENter A NUmber or press -1 to stop: "))
    if user_input2 != -1:
        totalIndex.append( user_input2)
        sumtotal = sumtotal+user_input2
        counter+=1
    else:
        print(totalIndex)
        print(sumtotal)
        average = sumtotal/counter
        print(round(average))
        break

    
tuple1 = 1,2,3, "mummy wa"
print(tuple1)


pi = 3.14159
radius = 2
circumference = 2 * pi * radius
print(round(circumference))

user_input = int(input("ENter a number:"))
if user_input % 2 == 0:
    print("Even")
else:
    print("Odd")



for number in range(0, 6):
    square = number*number
    cube = number*number*number
    print(number"\t"square"\t"cube)'''


sumnumber = 0
for num in range(0,3):
    user_input = int(input("Enter A Number:"))
    sumnumber+=user_input
print(sumnumber)





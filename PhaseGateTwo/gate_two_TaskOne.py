import random
for number in range(1,11):
    number1 = (random.randrange(1,50))
    mylist = [number1]
    print(number1, end = " ")


mylist = [1,3,4,5,7,8,9,2,6,7]
index = 0
for num in mylist:
    index+=1
    total = index
    print(total)
    
#print (len(mylist))


mylist = [1,3,5,6,7,8]
total = 0

for num in mylist:
    total+=num
    average = total / len(mylist)
print("sum is:", total)
print("average is: ",average)


mylist = [0, 1, 2, 3, 4, 5]
total = 0
for number in range(len(mylist)):
    if number%2 == 0:
        total += mylist[number]
print(total)


mylist = [0, 1, 2, 3, 4, 5]
total = 0
for number in range(len(mylist)):
    if number%2 !=0: 
        total += mylist[number]
print(total)

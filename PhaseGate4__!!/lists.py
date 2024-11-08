'''lst_zeros = [[0]*4 for _ in range(5)]
print(lst_zeros)
 
lst_zeros = [[0]*4]*5
print(lst_zeros)

for row in range(len(lst_zeros)):
    for col in range(len(lst_zeros[row])):
        print(lst_zeros[row][col], end =" ")
    print()


try:
    user_input = int(input("ENter A Number Between 1 and 10:"))
    user_input_two = int(input("ENter A Number Between 1 and 10:"))
    if user_input < 0 and user_input_two < 0:
        print("invalid")
        
    lists = [[0]*user_input]*user_input_two
#print(lists)

    for row in range(len(lists)):
        for column in range(len(lists[row])):
            product = lists[row][column]
            product = row * column
            print(" ", product, end = " \t")
        print()
except:
    print("Cheese")

#descending order
c = [5,2,7,1,8,2]
for i in range(len(c)):
    for j in range(len(c)):
        if c[i] > c[j]:
            temp = c[i]
            c[i] = c[j]
            c[j] = temp
print("Descending Order:", c)

#ascending order
c = [5,2,7,1,8,2]
for i in range(len(c)):
    for j in range(len(c)):
        if c[i] < c[j]:
            temp = c[i]
            c[i] = c[j]
            c[j] = temp
if c[i]%3 == 0:
    multiply = i*i
print("Ascending Order: ", c)
print(multiply)

c = [5,2,7,1,8,2]
for i in range(len(c)):
    product = c[i]*c[i]
    print(product, end = " ")
  


a = []
for number in range(1,6):
    a+=[number]
print(a)
'''
 def cube_list():
     for i in range(10):
         
s

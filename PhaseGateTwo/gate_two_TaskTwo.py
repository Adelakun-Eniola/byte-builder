for number in range(1000, 1201):
    while number != 0:
        remainder = number % 1000
        newnumber = number //1000
        if newnumber %2 !=0:
            break
        else:
            continue
        remainder1 = remainder %100
        newnumber1 = remainder1//100
        if newnumber1 % 2 != 0:
            break
        else:
            continue
    print(number)


'''
oddnumber = ["1"]
mylist = [1000]
for number in range(1001, 3001):
    mylist.append(number)
print(mylist)

for index in mylist:
    mylist.remove(oddnumber)
'''


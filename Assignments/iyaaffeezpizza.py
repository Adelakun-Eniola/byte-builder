menu = """
1. Sapa Size  ||(4 Slices Per Pack) || 2,000 per box
2. Small Money||(6 Slices)          || 2,400 per box
3. Big Boys   ||(8 Slices)          || 3,000 per box
4. Odogwu(    ||12 Slices)          || 4,200
"""
print(menu)
def myfunction():
    sapasize = 4
    smallmoney = 6
    bigboys = 8
    odogwu = 12

    sapasize_price = 2000
    smallmoney_size = 2400
    bigboys_price= 3000
    odogwu_price = 4200

    newsecondtotal = 0
    newbigboytotal = 0
    newsmallmoneytotal = 0
    newsapasizetotal = 0
    
    user = print(int(input("Select Pizza type: ")))
    people = print(int(input("How many people you wanna order for: ")))


    match user:
        case 1:
           def firstcase():
               
               print("you chose sapa size")
               sapaatotal = people % sapasize
               newsapasizetotal = people / sapasize

               if sapaatotal != 0:
                   
                   newsapasizetotal =  +1
                   print("num of box bought is: "+ newsapasizetotal)

                else:
                    
                    print(sapasizetotal + "is num of box")
                    
                remainingslice1 = people - (sapasizetotal * sapasize)
                print("remains: " + remainingslice1)

                totalamountone = sapasizetotal * sapasize_price
                print("toal amount: " + totalamountone)
               
            firstcase()
        case 2:
            
myfunction()

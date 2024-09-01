 
BASE_PAY = 5000
#amount_per_percel = 160


def logistics():
    delivery_rate = int(input("How many Successful Delivery Was Made: "))
    if delivery_rate >= 70:
        AMOUNT_PER_PERCEL = 500
        total_fee = (delivery_rate * AMOUNT_PER_PERCEL) + BASE_PAY
        return total_fee
    elif delivery_rate >= 60 and delivery_rate <= 69:
        AMOUNT_PER_PERCEL = 250
        total_fee = (delivery_rate * AMOUNT_PER_PERCEL) + BASE_PAY
        return total_fee
    elif delivery_rate >= 50 and delivery_rate < 59:
        AMOUNT_PER_PERCEL = 200
        total_fee = (delivery_rate * AMOUNT_PER_PERCEL) + BASE_PAY
        return total_fee
    else:
        AMOUNT_PER_PERCEL = 160
        total_fee = (delivery_rate * AMOUNT_PER_PERCEL) + BASE_PAY
        return total_fee
    
  

print("Your Wage For The Day Is: #",logistics())
    
    

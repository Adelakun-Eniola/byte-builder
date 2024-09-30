days_of_the_week = """
    0 -> Sunday
    1 -> Monday
    2 -> Tuesday
    3 -> Wednesday
    4 -> Thursday
    5 ->Friday
    6 -> Saturday
"""
inputed = int(input("ENter Today's Day:"))
elapsed_day = int(input("Enter The number of days elapsed since today:  "))



def elapsed_days():
    match elapsed_day:
            case 1:
                print("And the future day is Monday")
                
            case 2:
                print("And the future day is Tuesday")
                
            case 3:
                print("And the future day is Wednesday")
                
            case 4:
                print("And the future day is Thursday")
                
            case 5:
                print("And the future day is Friday")
                
            case 6:
                print("And the future day is Saturday")
                
elapsed_days()
    

match inputed:
    case 0:
        print("Today Is Sunday")
        elapsed_days()
        
    case 1:
        print("Today is Monday")
        elapsed_days()

    case 2:
        print("Today is Tuesday")
        elapsed_days()
    case 3:
        print("Today is Wednesday")
        elapsed_days()
    case 4:
        print("Today is Thursday")
        elapsed_days()
    case 5:
        print("Today is Friday")
        elapsed_days()
    case 6:
        print("Today is Saturday")
        elapsed_days()

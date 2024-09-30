def get_cube(number):
    if number < 0:
        raise ValueError("Invalid")
    
    return number **3

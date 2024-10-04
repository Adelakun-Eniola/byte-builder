number = 456

def reverse(number):
    
    original_num = number
    reverse_number = 0
    while number !=0:
        reverse_number = reverse_number*10 + number %10
        nuber = number //10
    
    return reverse_number, original_num

reverse(number)

print(reverse_number)

def isPalindrome(number, reverse_num):
    if original_num == reverse_num:
        return True
    else:
        return False
isPalindrome(original_num,reverse_num)

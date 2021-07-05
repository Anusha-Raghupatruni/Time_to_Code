

def isPalindrome(string):
    return string == string[::-1]
     
def iterative_method(string):

    for i in range(0,int(len((string))/2)):
        if string[i] != string[len(string)-i-1]:
            return False
    return True

def check_Palindrome(number):
    original = number
    reverse_num = 0
    while(number>0):
        remainder = number % 10
        reverse_num = reverse_num*10+remainder
        number //= 10
    if original == reverse_num:
        print("Palindrome")
    else:
        print("Not Palindrome")
number = 12345678
check_Palindrome(number)


        

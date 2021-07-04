def Add(num1,num2):

    while(num2!=0):
        carry = num1 & num2
        num1 = num1^num2
        num2 = carry<<1
    return num1


def recursive_Add(x,y):
    if (y==0):
        return x
    else:
        return recursive_Add(x^y,(x&y) << 1)
print(recursive_Add(32,61))


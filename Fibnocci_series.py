def fibonacci(n):
    if n<0:
        print("Incorrect input")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonocci(n-1)+fibonocci(n-2)
#print(fibonacci(5))

def fibonacci(n):
    f = [0,1]
    for i in range(2,n):
        f.append(f[i-1]+f[i-2])
    return f[n]
#print(fibonacci(9))

def fibonacci(n):
    first = 0
    second = 1
    if n<0:
        print("Incorrect input")
    elif n == 0:
        return first
    elif n == 1:
        return second
    else:
        for i in range(2,n+1):
            c = first + second
            first = second
            second = c
        return second
#print(fibonacci(9))

def fibonacci_sum(n):
    f = [0,1]
    fib_sum = 0
    for i in range(2,n+1):
        f.append(f[i-1]+f[i-2])
    for i in range(len(f)):
        fib_sum = fib_sum +f[i]
    return fib_sum

#print(fibonacci_sum(5))
        
def fib_Sum(n):
    if n == 0:
        return 0
    Sum = 0
    a,b = 1,1
    Sum += a
    while b<=n:
        Sum += b
        a,b = b,a+b
    return Sum

print(fib_Sum(5))











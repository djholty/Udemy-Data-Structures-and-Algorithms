
#solve using divide and conquer approach
#goal: get the value of the Nth number in the fibonacci series

def fibonacci(n):
    #base cases
    if n == 1:
        return 0
    elif n == 2 or n ==3:
        return 1
    else:        
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))


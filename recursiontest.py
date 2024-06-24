def firstmethod():
    print("Doing stuff in the first method before calling second")
    secondmethod()
    print('I am the first, now executing off stack')

def secondmethod():
    print("Doing stuff in the second method before calling third")
    thirdmethod()
    print('I am the second, now executing off stack')

def thirdmethod():
    print("Doing stuff in the third method before calling forth")
    fourthmethod()
    print('I am the third, now executing off stack')

def fourthmethod():
    print("Doing stuff in the forth method")

#firstmethod()

def recursivemethod(n):
    if n<1:
        print("n is less than 1")
    else:
        recursivemethod(n-1)
        print(n)

#recursivemethod(4)

def poweroftwo(n):
    if n==0:
        return 1
    else:
        power = poweroftwo(n-1)
        return power *2

#print(poweroftwo(4))

# 3 step approach to writing a recursive function:

# Factorial:
# n!
# 0! = 1
# product of all integers n to 1
# 4! = 4x3x2x1


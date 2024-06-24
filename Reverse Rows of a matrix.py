#Reverse rows of a matrix with iteration and swapping

def reverserows(array):
    n = len(array)
    for i in range(n//2): #use integer division to round down to nearest whole integer
        array[i], array[-(i+1)] = array[-(i+1)], array[i] 

myarray1 = [1,2,3,4,5,6,7,8,9,10]
myarray2 = [1,2,3,4,5,6,7,8,9]

reverserows(myarray1)
reverserows(myarray2)

print(myarray1)
print(myarray2)
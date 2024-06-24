# Find the missing number in an array
# My solution uncommented
def missing_number(arr, n):
    for i in range(n):
        if i+1 == arr[i]:
            continue
        else: 
            return i+1

# ALternative Solution
# def missing_number(arr, n):
#     # Calculate the sum of first n natural numbers
#     total = n * (n + 1) // 2
    
#     # Calculate the sum of numbers in the array
#     sum_arr = sum(arr)
    
#     # Find the missing number by subtracting sum_arr from total
#     missing = total - sum_arr
    
#     return missing
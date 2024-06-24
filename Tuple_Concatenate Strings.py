"""
Concatenate

Write a function that takes a tuple of strings and concatenates them, 
separating each string with a space.

Example

    input_tuple = ('Hello', 'World', 'from', 'Python')
    output_string = concatenate_strings(input_tuple)
    print(output_string)  # Expected output: 'Hello World from Python'
"""
#my code
def concatenate_strings(input_tuple):
    newstring = " ".join(input_tuple)
    return newstring

input_tuple = ('Hello', 'World', 'from', 'Python')
output_string = concatenate_strings(input_tuple)
print(output_string)

# #course solution
# SOLUTION - Time and Space Complexity of Concatenate

#     def concatenate_strings(input_tuple):
#         return ' '.join(input_tuple)

# Explanation

#     def concatenate_strings(input_tuple): - Define a function called 
#     "concatenate_strings" that takes a tuple of strings "input_tuple" as an argument.

#     return ' '.join(input_tuple) - Use the join method on a space character 
#     ' ' to concatenate the strings in the input tuple "input_tuple" with a space 
#     as the separator. Return the resulting concatenated string.

# Time and Space Complexity

#     def concatenate_strings(input_tuple): - Define a function called 
#     "concatenate_strings" that takes a tuple of strings "input_tuple" as an 
#     argument. No time or space complexity associated with this line as it is 
#     just a function definition.

#     return ' '.join(input_tuple) - This line uses the join method on a space 
#     character ' ' to concatenate the strings in the input tuple "input_tuple" 
#     with a space as the separator. The join method has a linear time complexity 
#     O(n) because it iterates through each string in the input tuple. The space 
#     complexity is also O(n) because it creates a new concatenated string with 
#     the length equal to the sum of the lengths of the strings in the input tuple 
#     plus the spaces in between.

# The overall time complexity of the function is O(n) because it iterates through 
# the strings in the input tuple once to create a new concatenated string. The 
# overall space complexity is O(n) because it creates a new concatenated string 
# with the length equal to the sum of the lengths of the strings in the input tuple 
# plus the spaces in between.

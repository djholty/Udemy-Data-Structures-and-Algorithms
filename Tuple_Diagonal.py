"""
Diagonal

Create a function that takes a tuple of tuples and returns a tuple containing the 
diagonal elements of the input.

Example

    input_tuple = (
        (1, 2, 3),
        (4, 5, 6),
        (7, 8, 9)
    )
    output_tuple = get_diagonal(input_tuple)
    print(output_tuple)  # Expected output: (1, 5, 9)

"""
#my solution
def get_diagonal(tup):
    diaglist = []
    for i, row in enumerate(tup):
        diaglist.append(row[i])
    return tuple(diaglist)

#course solution
# SOLUTION - Time and Space Complexity of Diagonal

#     def get_diagonal(input_tuple):
#         return tuple(input_tuple[i][i] for i in range(len(input_tuple)))

# Explanation

#     def get_diagonal(input_tuple): - Define a function called "get_diagonal" 
#     that takes a tuple of tuples "input_tuple" as an argument.

#     return tuple(input_tuple[i][i] for i in range(len(input_tuple))) - 
#     Use a generator expression to iterate through the indices i from 0 to the length 
#     of the input tuple minus one, and select the diagonal elements by indexing the 
#     inner tuples with the same index i. Create a new tuple containing the selected 
#     diagonal elements and return it.

# Time and Space Complexity

#     def get_diagonal(input_tuple): - Define a function called "get_diagonal" that 
#     takes a tuple of tuples "input_tuple" as an argument. No time or space complexity 
#     associated with this line as it is just a function definition.

#     return tuple(input_tuple[i][i] for i in range(len(input_tuple))) - This line uses 
#     a generator expression to iterate through the indices i from 0 to the length of 
#     the input tuple minus one, and select the diagonal elements by indexing the inner 
#     tuples with the same index i. The time complexity is O(n), where n is the length 
#     of the input tuple because it iterates through the indices once. The space 
#     complexity is O(n) because it creates a new tuple containing the diagonal elements, 
#     which has a length equal to the length of the input tuple.

# The overall time complexity of the function is O(n) because it iterates through the 
# indices of the input tuple once to create a new tuple with the diagonal elements. 
# The overall space complexity is O(n) because it creates a new tuple containing the 
# diagonal elements, which has a length equal to the length of the input tuple.
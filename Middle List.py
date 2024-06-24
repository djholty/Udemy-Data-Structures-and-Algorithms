# Middle Function

# Write a function called middle that takes a list 
# and returns a new list that contains all but the 
# first and last elements.

#My Solution
def middle(lst):
    newlist = lst[1:-1]
    return newlist

#course solution is the same
# Time Complexity:

# The function middle has a time complexity of O(n) where n is 
# the length of the input list lst. The reason is that slicing a 
# list takes linear time proportional to the length of the slice. In this case, the slice goes from index 1 to the second-last index, so the length of the slice is n - 2, which is still in the order of O(n).

# Space Complexity:

# The space complexity of the function is also O(n) because 
# it returns a new list that is a slice of the original list. 
# The new list has n - 2 elements, which is still in the order 
# of O(n). The memory usage is proportional to the length of 
# the input list lst.
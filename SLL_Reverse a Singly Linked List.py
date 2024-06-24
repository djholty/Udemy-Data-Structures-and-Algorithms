"""
Reverse a Singly Linked List

Write a function to reverse a singly linked 
list. The function should reverse the original
linked list.

Example:

Original singly linked list:   
1 -> 2 -> 3 -> 4 -> 5

Reversed singly linked list:  
5 -> 4 -> 3 -> 2 -> 1
"""
#my code
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' -> '
            temp_node = temp_node.next
        return result
    
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        
    def reverse(self):
        # TODO
        elementlist = []
        tempnode = self.head
        elementlist.append(tempnode.value)
        #store all values of linked list in regular list
        for _ in range(self.length-1):
            tempnode = tempnode.next
            elementlist.append(tempnode.value)
        elementlist.reverse() #reverse the list
        #iterate the linked list again updating all values
        tempnode = self.head
        
        tempnode.value = elementlist[0]
        for i in range(self.length -1):
            tempnode = tempnode.next
            tempnode.value = elementlist[i+1]
        
newlist = LinkedList()
newlist.append(10)
newlist.append(20)
newlist.append(30)
newlist.append(40)
print(newlist)
newlist.reverse()
print(newlist)

#course solution
    # def reverse(self):
    #     prev_node = None
    #     current_node = self.head
    #     while current_node is not None:
    #         next_node = current_node.next
    #         current_node.next = prev_node
    #         prev_node = current_node
    #         current_node = next_node
    #     self.head, self.tail = self.tail, self.head

# Explanation

#     def reverse(self): Defines a method named reverse in the LinkedList class.

#     prev_node = None: Initializes prev_node to None. It keeps track of the previous node during traversal.

#     current_node = self.head: Initializes current_node with the head of the linked list. The reverse operation starts from here.

#     while current_node is not None: Starts a while loop that continues until the end of the linked list is reached.

#     next_node = current_node.next: Saves the next node before overwriting current_node.next in the next step.

#     current_node.next = prev_node: Reverses the link by setting the next of current_node to prev_node.

#     prev_node = current_node: Updates prev_node to current_node for the next iteration.

#     current_node = next_node: Moves the current_node one step forward for the next iteration.

#     self.head, self.tail = self.tail, self.head: After the end of the loop, the head and tail are swapped to complete the reversal of the linked list.

# Time and Space Complexity

#     def reverse(self):

#         Time Complexity: O(1) - Constant time as it's just a function declaration.

#         Space Complexity: O(1) - No extra space used.

#     prev_node = None:

#         Time Complexity: O(1) - Assignment operations take constant time.

#         Space Complexity: O(1) - Only one variable is being used.

#     current_node = self.head:

#         Time Complexity: O(1) - Again, assignment operations are constant.

#         Space Complexity: O(1) - Only one variable is being used.

#     while current_node is not None:

#         Time Complexity: O(n) - This loop runs for all n nodes in the linked list.

#         Space Complexity: O(1) - No extra space is used within the loop.

#     next_node = current_node.next:

#         Time Complexity: O(1) - It's an assignment operation done inside the loop.

#         Space Complexity: O(1) - Only one variable is being used.

#     current_node.next = prev_node:

#         Time Complexity: O(1) - Assignment operation taking constant time.

#         Space Complexity: O(1) - No extra space being used.

#     prev_node = current_node:

#         Time Complexity: O(1) - Another assignment operation.

#         Space Complexity: O(1) - No extra space being used.

#     current_node = next_node:

#         Time Complexity: O(1) - Assignment operation.

#         Space Complexity: O(1) - No extra space being used.

#     self.head, self.tail = self.tail, self.head:

#         Time Complexity: O(1) - Assignment operation which is constant.

#         Space Complexity: O(1) - No extra space being used.

# Overall, the time complexity for the entire reverse function is O(n) as it traverses all n nodes once, and the space complexity is O(1) as it uses a constant amount of space throughout its execution.
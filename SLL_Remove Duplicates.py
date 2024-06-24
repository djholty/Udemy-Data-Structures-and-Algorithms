"""
Duplicates from a Singly Linked List

Given a singly linked list, write a function that removes all the duplicates. use this linked list .

Original Linked List - "1 -> 2 -> 4-> 3 -> 4->2"

Result Linked List - "1 -> 2 -> 4 -> 3

"""

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
    
    def remove_duplicates(self):
        # TODO
    #my solution
        if self.head is None:
            return

        items = set()
        currentnode = self.head
        previousnode = None

        while currentnode is not None:
            if currentnode.value in items:
                # If value is in set, delete the node
                if currentnode.next is not None:
                    previousnode.next = currentnode.next
                else: #deletion technique if last node is a duplicate
                    previousnode.next = None  # Update previous node's next to None if current node is the last node and its a duplicate
                self.length -= 1
                currentnode = currentnode.next  # Move to the next node
            else:
                items.add(currentnode.value)
                previousnode = currentnode
                currentnode = currentnode.next

        self.tail = previousnode  # Update tail if duplicates were removed

newlink = LinkedList()
newlink.append(10)
newlink.append(10)
newlink.append(20)
newlink.append(10)
newlink.append(20)
newlink.append(30)
newlink.append(10)
newlink.append(30)
newlink.append(40)
newlink.append(40)
print(newlink)
newlink.remove_duplicates()
print(newlink)

#course solution
#     def remove_duplicates(self):
#         if self.head is None:
#             return
#         node_values = set()  # set to store unique node values
#         current_node = self.head
#         node_values.add(current_node.value)
#         while current_node.next:
#             if current_node.next.value in node_values:  # duplicate found
#                 current_node.next = current_node.next.next
#                 self.length -= 1
#             else:
#                 node_values.add(current_node.next.value)
#                 current_node = current_node.next
#         self.tail = current_node

#         Explanation:

#     def remove_duplicates(self): This line is defining the function remove_duplicates 
#     within the LinkedList class.

#     if not self.head: This line checks if the head of the LinkedList is None, 
#     which would indicate that the list is empty.

#     return If the list is empty, the function ends execution and returns None.

#     unique_values = set([self.head.value]) If the list is not empty, the function 
#     creates a set unique_values and adds the value of the head node to it.

#     current_node = self.head The function sets current_node to the head of the list. 
#     This variable will be used to traverse the list.

#     while current_node.next: This line starts a while loop that will continue as 
#     long as the next attribute of the current_node is not None.

#     if current_node.next.value in unique_values: This line checks if the value of 
#     the next node is already in the set of unique values.

#     current_node.next = current_node.next.next If the value is in the set, this 
#     line removes the next node from the list by skipping over it and setting the 
#     next attribute of the current node to the node after the next node.

#     self.length -= 1 Since a node was removed, the length of the list is decremented 
#     by 1.

#     else: This is the other case where the value of the next node is not in the set.

#     unique_values.add(current_node.next.value) This line adds the value of the next 
#     node to the set of unique values.

#     current_node = current_node.next Since the next node is unique, we move forward 
#     to the next node.

#     self.tail = current_node After the loop, the current_node will be the last node 
#     in the list. So, we update the tail of the list to be current_node.

# Time Complexity:


#     if self.head is None: return: This line performs a constant time operation, O(1), 
#     as it only checks the value of self.head once.

#     node_values = set(): Creating an empty set takes constant time, O(1).

#     current_node = self.head: Assigning the head of the linked list to current_node 
#     takes constant time, O(1).

#     node_values.add(current_node.value): Adding the value of the current node to the 
#     set takes constant time, O(1).

#     while current_node.next:: This while loop iterates over the linked list until 
#     current_node.next becomes None. The number of iterations is proportional to the 
#     number of nodes in the linked list, let's call it 'n'.

#     Inside the loop:

#         if current_node.next.value in node_values:: This line checks if the value of 
#         the next node is in the set node_values. This operation performs a constant 
#         time lookup in the set, O(1).

#         If the condition is true:

#             current_node.next = current_node.next.next: This operation removes the 
#             next node by linking the current node to the node after the next node. 
#             It takes constant time, O(1).

#             self.length -= 1: Decrementing the length of the linked list takes 
#             constant time, O(1).

#         If the condition is false:

#             node_values.add(current_node.next.value): Adding the value of the next 
#             node to the set takes constant time, O(1).

#             current_node = current_node.next: Moving to the next node takes constant 
#             time, O(1).

#     self.tail = current_node: Assigning current_node to self.tail takes constant time, 
#     O(1).

# Overall, the time complexity of the remove_duplicates method is O(n), where n is the 
# number of nodes in the linked list. This is because the while loop iterates through 
# the list once, performing constant-time operations in each iteration.

# Space Complexity:

# node_values = set(): Creating the set to store unique node values takes constant space, 
# O(1).

# The space complexity of the remove_duplicates method is O(1), as the space used does 
# not grow with the size of the input. It only requires a constant amount of extra space 
# to store the set node_values.

# In summary, the method has a time complexity of O(n) and a space complexity of O(1), 
# making it efficient in terms of both time and space usage.



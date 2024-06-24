"""
Insertion at the Beginning of a Singly Linked List
Write a function to insert a new element at the beginning of a singly 
linked list. LinkedList and Node class are already provided.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0
        
    # Implement Here # my code
    def prepend(self,value):
        newnode =  Node(value)
        newnode.next = self.head
        self.head = newnode
        self.length += 1

# # course solution:
#     def prepend(self, value):
#             new_node = Node(value)
#             new_node.next = self.head
#             self.head = new_node
#             self.length += 1
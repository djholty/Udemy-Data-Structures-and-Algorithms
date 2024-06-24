class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def __str__(self):
        return str(self.value)

class CSLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            temp_node = temp_node.next
            if temp_node == self.head:  # Stop condition for circular list
                break
            result += ' -> '
        return result
    
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        self.length += 1
    
    def delete_by_value(self, value):
        # TODO
        # my solution
        target = value
        cursor = self.head
        previous = None
        while cursor:
            if self.length == 0:
                return None
            #iterate through the linked list checking if node value is the target
            # check special cases like first node, last node, and middle nodes

            #head node check
            if cursor.value == target and cursor is self.head:
                self.head = cursor.next
                cursor.next = None
                self.length -= 1
                return cursor

            #tail node check
            if cursor.value == target and cursor is self.tail:
                previous.next = None
                self.tail = previous
                self.length -= 1
                return cursor

            #middle node check
            if cursor.value == target and (cursor is not self.head and cursor is not self.tail):
                previous.next = cursor.next
                cursor.next = None
                self.length -= 1
                return cursor
            
            previous = cursor
            cursor = cursor.next
            if cursor == self.head:
                break
        return None

#course solution:
#     class Node:
#         def __init__(self, value):
#             self.value = value
#             self.next = None
        
#         def __str__(self):
#             return str(self.value)
     
#     class CSLinkedList:
#         def __init__(self):
#             self.head = None
#             self.tail = None
#             self.length = 0
        
#         def __str__(self):a
#             temp_node = self.head
#             result = ''
#             while temp_node is not None:
#                 result += str(temp_node.value)
#                 temp_node = temp_node.next
#                 if temp_node == self.head:  # Stop condition for circular list
#                     break
#                 result += ' -> '
#             return result
        
#         def append(self, value):
#             new_node = Node(value)
#             if self.length == 0:
#                 self.head = new_node
#                 self.tail = new_node
#                 new_node.next = new_node
#             else:
#                 self.tail.next = new_node
#                 new_node.next = self.head
#                 self.tail = new_node
#             self.length += 1
        
#         def delete_by_value(self, value):
#             if self.length == 0:  # If the list is empty
#                 return False
     
#             # Handle the case where the list has only one node
#             if self.head == self.tail and self.head.value == value:
#                 self.head = None
#                 self.tail = None
#                 self.length = 0
#                 return True
     
#             prev = None
#             current = self.head
#             while True:
#                 if current.value == value:  # Node to delete is found
#                     if current == self.head:  # Node is at the head
#                         self.head = current.next
#                         self.tail.next = self.head
#                     else:
#                         prev.next = current.next
#                         if current == self.tail:  # Node is at the tail
#                             self.tail = prev
                    
#                     self.length -= 1
#                     return True
     
#                 prev = current
#                 current = current.next
#                 if current == self.head:  # If we have traversed the entire list
#                     break
     
#             return False  # Node with the value was not found

# The delete_by_value method in the CSLinkedList class is designed to find and remove the first node in the circular singly linked list (CSLL) that contains a specific value. Let's break down the method line by line:

#     if self.length == 0: - Check if the list is empty. If it is, there's no node to delete, so the method returns False.

#     if self.head == self.tail and self.head.value == value: - This checks if there is only one node in the list (self.head == self.tail) and if that node's value matches the value we want to delete (self.head.value == value).

#     self.head = None - If the above condition is true, set head to None, effectively removing the only node from the list.

#     self.tail = None - Similarly, set tail to None, leaving the list empty.

#     self.length = 0 - Adjust the length of the list to 0 since we've removed the only node.

#     return True - Return True to indicate that the node was successfully deleted.

#     prev = None - Initialize a prev variable to None. This will be used to keep track of the node preceding the current node during the traversal.

#     current = self.head - Start the traversal from the head of the list.

#     while True: - Begin an infinite loop to traverse the list. The loop will break internally once the node is deleted or the list is fully traversed.

#     if current.value == value: - Check if the current node's value matches the value to be deleted.

#     if current == self.head: - If the node to be deleted is the head, update self.head to the next node.

#     self.head = current.next - Set the head to the next node in the list.

#     self.tail.next = self.head - Update the tail's next pointer to point to the new head, maintaining the circular nature of the list.

#     else: - If the node to be deleted is not the head...

#     prev.next = current.next - Bypass the current node by setting the previous node's next to the current node's next.

#     if current == self.tail: - Check if the node to be deleted is the tail.

#     self.tail = prev - If it is, update self.tail to the previous node.

#     self.length -= 1 - Decrease the length of the list by 1 since a node has been removed.

#     return True - Return True to indicate that the node was successfully deleted.

#     prev = current - Before moving to the next node, set prev to the current node.

#     current = current.next - Move to the next node in the list.

#     if current == self.head: - Check if we have traversed the entire list (back to the head).

#     break - If we are back at the head, break out of the loop.

#     return False - If the loop completes without finding a node to delete, return False to indicate that no node with the given value was found.

# Time Complexity:

#     The worst-case time complexity is O(n), where n is the number of nodes in the list. This is because, in the worst-case scenario, the method might need to traverse the entire list to find the node to delete.

# Space Complexity:

#     The space complexity is O(1) since the method uses a constant amount of space regardless of the size of the input list.
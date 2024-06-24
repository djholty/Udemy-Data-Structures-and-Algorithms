 
"""
 Method to count the number of nodes in a
 CSLL
"""
 
 
 
 #TODO
def count_nodes(self):
    cursor = self.head
    count = 0
    if cursor is None:
        return 0
    while True:
        count += 1
        cursor = cursor.next
        if cursor == self.head:
            break
    return count

#course solution
#  #TODO
#     def count_nodes(self):
#         cursor = self.head
#         count = 0
#         if cursor is None:
#             return 0
#         while True:
#             count += 1
#             cursor = cursor.next
#             if cursor == self.head:
#                 break
#         return count
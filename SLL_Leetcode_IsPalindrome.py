class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def isPalindrome(self, head):
        #my solution
        cursor = head
        itemlist = list()
        while cursor:
            itemlist.append(cursor.val)
            cursor = cursor.next
        for i in range(len(itemlist)//2):
            #compare the first and last, second and second last etc..
            if itemlist[i] != itemlist[-(i+1)]:
                return False
            else:
                continue
        return True

#course solution 
#     class ListNode(object):
#         def __init__(self, val=0, next=None):
#             self.val = val
#             self.next = next
     
#     class Solution(object):
#         def isPalindrome(self, head):
#             slow = fast = head
#             while fast and fast.next:
#                 slow = slow.next
#                 fast = fast.next.next
     #   this first loop positions a pointer at the middle node using the tortoise and hare algo
#             prev = None
#             while slow:
#                 nxt = slow.next
#                 slow.next = prev
#                 prev = slow
#                 slow = nxt
 #              the second loop through reverses the direction of the list from the end to the middle 
#             while prev:
#                 if head.val != prev.val:
#                     return False
#                 head = head.next
#                 prev = prev.next
#             return True
   #finally the last loop through iterates through these two new lists and compares each value 
#                 class Solution:

#     Here we're declaring a class named "Solution".

#     def isPalindrome(self, head):

#     This line is defining a method named isPalindrome within the Solution class. It takes self and head as parameters. The head is a reference to the head of the linked list.

#     slow = fast = head

#     Here we're setting both slow and fast to start at the head of the linked list. These are pointers that will be used to traverse the linked list.

#     while fast and fast.next:

#     This line begins a loop that will continue until the fast pointer reaches the end of the list. The fast pointer moves twice as fast as the slow pointer. So, by the time fast reaches the end, slow will be at the midpoint of the list.

#     slow = slow.next and fast = fast.next.next

#     Inside the loop, we're moving slow one step forward and fast two steps forward in each iteration. This is how we ensure slow is at the midpoint when fast reaches the end.

#     prev = None

#     We're initializing prev to None before starting to reverse the second half of the linked list.

#     while slow:

#     This loop will reverse the second half of the linked list. It continues until all nodes in the second half are visited.

#     nxt = slow.next

#     Here we're saving the next node of slow before changing its reference.

#     slow.next = prev

#     This line is making the slow node point back to the previous node, which is the essence of reversing the list.

#     prev = slow and slow = nxt

#     Here, we're moving prev one step forward and then moving slow to its next node (saved in nxt).

#     while prev:

#     This loop will continue as long as there are nodes in the reversed list (prev).

#     if head.val != prev.val: return False

#     Inside this loop, we're comparing the node values of the first half and the second half (reversed). If any pair of nodes have different values, we return False, implying the list is not a palindrome.

#     head = head.next and prev = prev.next

#     We're moving the pointers of the original list (head) and reversed list (prev) one step forward for the next comparison in each iteration.

#     return True

#     If the control reaches this line, it means all pairs of nodes have been checked and none have mismatched. Hence, we return True because the linked list is a palindrome.

# Time and Space Complexity


#     slow = fast = head

#     The assignment operation is constant time, O(1), and does not require additional space, so it's also O(1).

#     while fast and fast.next:

#     This loop traverses the list until fast reaches the end, which is half the list length because fast moves twice as fast as slow. This is O(n/2) = O(n) in terms of time complexity. We're not using any additional space, so it's O(1) in space complexity.

#     slow = slow.next and fast = fast.next.next

#     These operations inside the loop are constant time, O(1), and do not use additional space, hence O(1) in space complexity.

#     prev = None

#     This operation is O(1) in time and space complexity.

#     while slow:

#     This loop traverses the second half of the list. So, its time complexity is O(n/2) = O(n), and space complexity is O(1) as no additional space is used.

#     nxt = slow.next, slow.next = prev, prev = slow and slow = nxt

#     These operations inside the loop are all constant time, O(1), and constant space, O(1).

#     while prev:

#     This loop traverses the second half of the list. So, its time complexity is O(n/2) = O(n), and space complexity is O(1) as no additional space is used.

#     if head.val != prev.val: return False, head = head.next and prev = prev.next

#     These operations inside the loop are all constant time, O(1), and constant space, O(1).

#     return True

#     Returning a value is a constant time operation, O(1), and does not require any additional space, O(1).

# In total, the time complexity of the function is O(n) because each operation involving n is linear. The space complexity is O(1) as no extra space dependent on the size of the linked list is used.
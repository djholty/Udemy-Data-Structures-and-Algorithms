class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
 
class Solution(object):
    def middleNode(self, head):
        slow = head
        fast = head

        while fast and fast.next: 
            #need to stop when fast.next is None otherwise loop 
            #will run an extra time and slow will pass the middle node
            #and also will try to access None.next which will raise error
            slow = slow.next
            fast = fast.next.next
        return slow

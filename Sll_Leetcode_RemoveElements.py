"""
Remove Linked List Elements

Given the head of a linked list and an integer
 val, remove all the nodes of the linked list 
 that has Node.val == val, and return the new 
 head.

"""




class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeElements(self, head, val):
        # TODO - my solution
        dummynode = ListNode(-1)
        dummynode.next =  head
        current = head
        target =  val
        previous = dummynode
        while current:
            if current.val == target:
                previous.next = current.next
            else:
                previous = current
            current = previous.next
        return dummynode.next

 #course solution
 #     class ListNode(object):
    #     def __init__(self, val=0, next=None):
    #         self.val = val
    #         self.next = next
     
    # class Solution(object):
    #     def removeElements(self, head, val):
    #         dummy_head = ListNode(-1)
    #         dummy_head.next = head
     
    #         prev_node, curr_node = dummy_head, head
    #         while curr_node:
    #             if curr_node.val == val:
    #                 prev_node.next = curr_node.next
    #             else:
    #                 prev_node = curr_node
    #             curr_node = curr_node.next
     
    #         return dummy_head.next       
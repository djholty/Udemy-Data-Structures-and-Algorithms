# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, l1, l2):
            """
            :type list1: Optional[ListNode]
            :type list2: Optional[ListNode]
            :rtype: Optional[ListNode]
            """
            dummynode = ListNode(-1)
            mergelist = dummynode
            
            while l1 and l2:
                if l1.val <= l2.val:
                    mergelist.next = l1 #move l1 cursor forward
                    l1 = l1.next
                else:
                    mergelist.next = l2  #move l2 cursor forward
                    l2 = l2.next
                mergelist = mergelist.next #move merglist forward
            mergelist.next = l1 if l1 is not None else l2
            
            return dummynode.next #return first node in merged list


#course explanation
    #         Time and Space Complexity

    # class ListNode:

    #     def __init__(self, val=0, next=None):

    #         self.val = val

    #         self.next = next

    # Time complexity: O(1) - Initialization takes constant time.

    # Space complexity: O(1) - A single node's memory allocation is constant.

    # def mergeTwoLists(l1, l2):

    # Time complexity: O(1) - Function definition does not involve any computation.

    # Space complexity: O(1) - No additional space is being used here.

    # prehead = ListNode(-1)

    # Time complexity: O(1) - Creating a single node takes constant time.

    # Space complexity: O(1) - Only one new node is being created, which requires constant space.

    # prev = prehead

    # Time complexity: O(1) - Assigning a reference takes constant time.

    # Space complexity: O(1) - No additional space is being used here.

    # while l1 and l2:

    #     if l1.val <= l2.val:

    #         prev.next = l1

    #         l1 = l1.next

    #     else:

    #         prev.next = l2

    #         l2 = l2.next

    #     prev = prev.next

    # Time complexity: O(n + m) - In the worst case scenario, we have to iterate through all nodes in both l1 and l2.

    # Space complexity: O(1) - We are not using any extra space that grows with the size of the input. We are only using a few pointers.

    # prev.next = l1 if l1 is not None else l2

    # Time complexity: O(1) - Assigning a reference takes constant time.

    # Space complexity: O(1) - No additional space is being used here.

    # return prehead.next

    # Time complexity: O(1) - Returning a value takes constant time.

    # Space complexity: O(1) - No additional space is being used here.




class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        #mysolution
        # TODO
        seenitems =  set()
        dummy = ListNode(-1)
        dummy.next = head
        current = head
        previous = None
        while current:
            if current.val in seenitems:  #then delete node
                previous.next = current.next
            else:
                seenitems.add(current.val)
                previous = current
            current = previous.next
        return dummy.next

        
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def print_list(self):
        nodes = []
        temp = self.head
        while temp:
            nodes.append(str(temp.data))
            temp = temp.next
            if temp == self.head:
                break
        print(" -> ".join(nodes))

    def is_sorted(self):
        # TODO
        #my solution
        if self.head == None:
            return True
        current = self.head
        previous = -1000000
        while current.next is not self.head:
            previous = current
            current = current.next
            if previous.data <= current.data:
                continue
            else:
                return False
        return True


        #course solution
    #             def is_sorted(self):
    #         if self.head is None:
    #             return True  # An empty list is considered sorted.
            
    #         temp = self.head
    #         while temp.next != self.head:
    #             if temp.data > temp.next.data:
    #                 return False
    #             temp = temp.next
     
    #         return True


    # def is_sorted(self):
    #     if self.head is None or self.head.next == self.head:
    #         return True  # An empty list or a single element list is considered sorted.
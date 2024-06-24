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
            self.head.next = new_node
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def print_list(self):
        if not self.head:
            print("The list is empty.")
            return
 
        nodes = []
        temp = self.head
        while True:
            nodes.append(str(temp.data))
            temp = temp.next
            if temp == self.head:
                break
        print(" -> ".join(nodes))



    def prepend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = new_node
        else:
            new_node.next = self.head
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            self.head = new_node


    def insert_into_sorted(self, data):
        # TODO
        #my solution
        cursor = self.head
        newnode = Node(data)
        previous = None
        if cursor == None: #checks if list is empty and then just inserts node
            self.head = newnode
            newnode.next = newnode
        while cursor: 
           
            if cursor.data > data and cursor == self.head: #if data is smaller than first node
                self.prepend(data)
            if previous: #makes sure previous is not None
                if cursor.data > data and data > previous.data: #find spot for data to fit in between two nodes and insert there
                    newnode.next = cursor
                    previous.next = newnode
            if cursor.data < data and cursor.next == self.head: #if data is bigger than last node
                self.append(data)
            if cursor.next == self.head:
                break
            previous = cursor
            cursor = cursor.next

clist = CircularLinkedList()
clist.insert_into_sorted(10)
clist.print_list()
clist.append(1)
clist.append(3)
clist.append(4)
clist.append(5)
clist.append(6)
clist.print_list()

#course solution
    # def insert_into_sorted(self, data):
    #     new_node = Node(data)
    #     if not self.head:
    #         self.head = new_node
    #         new_node.next = new_node
    #     elif data <= self.head.data:
    #         self.prepend(data)
    #     else:
    #         temp = self.head
    #         while temp.next != self.head and temp.next.data < data:
    #             temp = temp.next
    #         new_node.next = temp.next
    #         temp.next = new_node
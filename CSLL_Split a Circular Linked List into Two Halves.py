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

    def split_list(self):
        # TODO
        def split_list(self):
        # TODO
        first_list = CSLinkedList()
        second_list = CSLinkedList()
        if self.length == 0:
            return None, None
        if self.length == 1:
            return self
        
        cursor = self.head
        first_list.head = cursor #point firstlist head to first node
        middleindex = math.ceil(self.length//2) #find middle node giving first half extra node if odd number
        for i in range(middleindex+1):  #move to middle node
            cursor = cursor.next
        first_list.tail = cursor #point tail to last node 
        second_list.head = cursor.next #point second_list to head of second list
        for i in range(middleindex+1,self.length):
            cursor =  cursor.next
        second_list.tail = cursor
        cursor.next = second_list.head
    
        return first_list, second_list

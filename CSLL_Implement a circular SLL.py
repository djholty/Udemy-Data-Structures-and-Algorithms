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
#my solutions    
    def __str__(self):
        # TODO
        result = ""
        if self.length == 0:
            return None
        elif self.length == 1:
            return str(self.head.value)
        else:
            cursor = self.head
            while cursor is not self.tail:
                result += str(cursor.value)
                result += " -> "
                cursor = cursor.next
            result += str(cursor.value) #adds the value of the tail node
        return result


    
    def append(self, value):
        # TODO
        newnode = Node(value)
        if self.length == 0:
            self.head = newnode
            self.tail = newnode
            newnode.next = self.head
        else:
            self.tail.next = newnode
            newnode.next = self.head
            self.tail = newnode
        self.length += 1    
    
    def prepend(self, value):
        # TODO
        newnode = Node(value)
        if self.length == 0:
            self.head = newnode
            self.tail = newnode
            newnode.next = newnode
        else:
            newnode.next = self.head
            self.tail.next = newnode
            self.head = newnode
        self.length += 1


myCSLL = CSLinkedList()

myCSLL.append(10)
print(myCSLL)
myCSLL.append(20)
myCSLL.append(30)
print(myCSLL)

#course solutions


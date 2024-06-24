import QueueLinkedList as queue

class BSTNode:
    def __init__(self, data ):
        self.data = data
        self.leftChild = None
        self.rightChild = None

def preOrderTravesal(rootNode):
    if not rootNode:
        return
    print(rootNode)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)

def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode)
    inOrderTraversal(rootNode.rightChild)

def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode)

def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        customqueue = queue.Queue()
        customqueue.enqueue(rootNode)
        while not(customqueue.isEmpty()):
            root = customqueue.dequeue()
            print(root.value.data)
            if root.value.leftChild is not None:
                customqueue.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                customqueue.enqueue(root.value.rightChild)
        



def insertNode(rootNode, nodeValue):
    if rootNode.data == None:
        rootNode.data = NodeValue
    elif nodeValue <= rootNode.data: # compare nodeValue to root, if lower, go to left child
        if rootNode.leftChild is None:
            rootNode.leftChild = BSTNode(nodeValue)
        else:
            insertNode(rootNode.leftChild, nodeValue)
    else: # compares NodeValue to root node and goes to Right Child if bigger
        if rootNode.rightChild is None:
            rootNode.rightChild = BSTNode(nodeValue)
        else:
            insertNode(rootNode.rightChild, nodeValue)
    return "The node was successfully inserted"




def deleteNode(rootNode, nodeValue):
    if rootNode is None:
        return rootNode
    if nodeValue < rootNode.data:
        rootNode.leftChild = deleteNode(rootNode.leftChild, nodeValue)
    elif nodeValue > rootNode.data:
        rootNode.rightChild = deleteNode(rootNode.rightChild, nodeValue)
    else:
        if rootNode.leftChild is None:
            temp = rootNode.rightChild
            rootNode = None
            return temp
        
        if rootNode.rightChild is None:
            temp = rootNode.leftChild
            rootNode = None
            return temp 

        temp = minValueNode(rootNode.rightChild)
        rootNode.data = temp.data
        rootNode.rightChild = deleteNode(rootNode.rightChild, temp.data)
    return rootNode

def deleteBST(rootNode):
    rootNode.data = None
    rootNode.rightChild = None
    rootNode.leftChild = None
    return "The node has been successfully deleted"

        
newBST = BSTNode(10)
insertNode(newBST, 70)
insertNode(newBST, 60)
insertNode(newBST, 55) 
insertNode(newBST, 40)
insertNode(newBST, 30)
insertNode(newBST, 20)
insertNode(newBST, 25)

print(insertNode(newBST, 50))
print(newBST.rightChild.data)
print(newBST.rightChild.leftChild.data)
levelOrderTraversal(newBST)



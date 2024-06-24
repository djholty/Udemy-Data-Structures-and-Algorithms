
class TreeNode:
    def __init__(self, data, children =[]):
        self.data = data
        self.children = children

    def __str__(self, level=0):
        ret = "  " * level + str(self.data) + "\n"
        for child in self.children:
            ret += child.__str__(level +1)
            print(ret)
        return ret

    def addChild(self, TreeNode):
        self.children.append(TreeNode)

tree = TreeNode('Drinks', [])
cold = TreeNode('Cold Drinks', [])
hot = TreeNode('Hot', [])
tree.addChild(cold)
tree.addChild(hot)
pepsi = TreeNode("Pepsi", [])
smallpepsi = TreeNode("Small Pepsi", [])
largepepsi = TreeNode("Large Pepsi", [])
coke = TreeNode("Coke", [])
coffee = TreeNode("Coffee", [])
tea = TreeNode("Tea", [])
cold.addChild(pepsi)
cold.addChild(coke)
hot.addChild(coffee)
hot.addChild(tea)
pepsi.addChild(smallpepsi)
pepsi.addChild(largepepsi)
print(tree)
        
    
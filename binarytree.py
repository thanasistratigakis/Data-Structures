
class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    # if root doesnt exist, set root.  Else: traverse tree until leaf found
    def set(self,key,value):
        if self.root is not None:
            self._set(key, value, self.root)
        else:
            self.root = TreeNode(key, value)
            self.size = self.size + 1

    def _set(self, key, value, currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._set(key, value, currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key, value, parent=currentNode)
        else:
            if currentNode.hasRightChild():
                self._set(key, value, currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key, value, parent=currentNode)
    # returns node
    def search(self, key):
        if self.root:
            result = self._search(key, self.root)
            if result is not None:
               return result
            else:
               return None
        else:
            return None

    # returns value
    def _search(self,key,currentNode):
        print(currentNode)
        if not currentNode:
            return None
        elif currentNode.key == key:
            return currentNode.value
        elif key < currentNode.key:
            return self._search(key,currentNode.leftChild)
        else:
            return self._search(key,currentNode.rightChild)


    def delete(self, key):
        if self.size > 1:
            nodeToRemove = self._search(key, self.root)
            if nodeToRemove:
                self.remove(nodeToRemove)
                self.size = self.size - 1
            else:
                raise KeyError('Error, key not in tree')
        # handle delete root
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = self.size - 1
        else:
            raise KeyError('Error, key not in tree')

    def traverse(self, node):
        if node != None:
            self.traverse(node.hasLeftChild())
            print(node.value)
            self.traverse(node.hasRightChild())




class TreeNode:
    def __init__(self,key,value,left=None,right=None,parent=None):
        self.key = key
        self.value = value
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeaf(self):
        if not (self.rightChild or self.leftChild):
            return False
        else:
            return True


data = [("one", 1), ("two", 2), ("three", 3), ("four", 4), ("five", 5), ("six", 6)]

my_tree = BinarySearchTree()

for item in data:
    my_tree.set(item[0], item[1])

print my_tree
print(my_tree.search("five"))

my_tree.traverse(my_tree.root)






# comment

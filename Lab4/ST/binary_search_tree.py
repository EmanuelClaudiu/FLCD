class Node:

    def __init__(self, token = '', index = 0):
        self.token = token # identifier / constant / reserved word / operator / separator
        self.index = index
        self.leftChild = None
        self.rightChild = None
    
    def getToken(self):
        return self.token

    def getIndex(self):
        return self.index

    def get(self, token):
        found = None
        if token == self.token:
            # found the token
            found = True
            return self
        if found == None and self.isLeaf():
            # reached a leaf and did not find token
            return None
        if found == None and self.leftChild != None:
            found = self.leftChild.get(token)
        if found == None and self.rightChild != None:
            found = self.rightChild.get(token)
        return found
         

    def isLeaf(self):
        if self.leftChild == None and self.rightChild == None:
            return True
        else:
            return False

    def __str__(self):
        if self.isLeaf():
            return f'[T:{self.token}, I:{self.index}]'
        else:
            return f'[T:{self.token}, I:{self.index}, Left:{str(self.leftChild)}, Right:{str(self.rightChild)}]'

class BinarySearchTree():

    def __init__(self):
        self.root = None

    def insert(self, token, index):
        if self.root == None:
            # empty tree, configure root
            self.root = Node(token, index)
        else:
            # non-empty tree
            self.deep_insert(self.root, Node(token, index))

    def deep_insert(self, node, toInsert):
        # alphabetical comparrison
        if toInsert.getToken() > node.getToken():
            if node.rightChild == None:
                node.rightChild = toInsert
            else:
                self.deep_insert(node.rightChild, toInsert)
        else:
            if node.leftChild == None:
                node.leftChild = toInsert
            else:
                self.deep_insert(node.leftChild, toInsert)
    
    def search(self, token):
        return self.root.get(token)
    
    def __str__(self):
        return str(self.root)

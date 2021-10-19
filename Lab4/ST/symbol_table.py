from .binary_search_tree import BinarySearchTree

class SymbolTable:
    def __init__(self):
        self.table = BinarySearchTree()

    def insert(self, token, index):
        exists = None
        if self.table.root != None:
            exists = self.get(token)
        if exists == None:
            # if node does not exist, add it
            self.table.insert(token, index)
        else:
            # if node already exists, return index
            return exists.getIndex()
    
    def get(self, token):
        return self.table.search(token)

    def __str__(self):
        return str(self.table)
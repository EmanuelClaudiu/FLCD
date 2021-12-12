class Node:

    def __init__(self, element):
        self.element = ''
        self.children = []
        self.parent = None

    def init_kids(self, kids):
        for k in kids:
            self.children.append(Node(k))
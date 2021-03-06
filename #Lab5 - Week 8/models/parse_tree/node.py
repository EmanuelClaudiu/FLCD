import copy


class Node:

    def __init__(self, action_sheet, parent, NODES):
        self.action_sheet = action_sheet
        self.element = ''
        self.parent = parent
        self.children = []
        self.NODES = NODES

    def configure(self):
        if len(self.action_sheet) != 0:
            action = self.pop_from_head()
            if action not in ["accepted", "rejected"] and action[0] != "pop":
                self.element = action[0]
                children = action[1]
                for c in children:
                    new_node = Node(self.action_sheet, self, self.NODES)
                    self.children.append(new_node)
                    self.NODES.append(new_node)
                    if c == "@":
                        #self.action_sheet = [("pop", "@")] + self.action_sheet
                        self.action_sheet.insert(0, ("pop", "@"))
                for child in self.children:
                    child.configure()
            if action[0] == "pop":
                self.element = action[1]


    def pop_from_head(self):
        action = copy.deepcopy(self.action_sheet[0])
        del self.action_sheet[0]
        return action

    def __str__(self):
        parent = self.parent
        right_sibling = None
        try:
            i = parent.children.index(self)
            right_sibling = parent.children[i + 1].element
        except:
            pass
        return f"Element: {self.element} | Parent: {self.parent.element} | Right-sibling:{right_sibling}"

    def print_children(self):
        toReturn = ""
        if len(self.children) != 0:
            toReturn += f"{self.element}: ["
            for c in self.children:
                toReturn += c.print_children()
            toReturn += "], "
        else:
            toReturn += f"{self.element}, "
        return toReturn
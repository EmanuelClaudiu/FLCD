from parser import Parser
from grammar import Grammar
import copy
from parse_tree.node import Node
from parse_tree.tree import ParsingTree

class ParseTable:

    def __init__(self, parser):
        self.parser = parser
        self.grammar = self.parser.grammar
        self.table = {}
        self.stack = []
        self.input = []
        self.parseTree = None
        self.NODES = []
        self.init_table()
        self.create_table()

    def init_table(self):
        for non_terminal in self.grammar.non_terminals:
            set = {}
            for terminal in self.grammar.terminals:
                if terminal == "@":
                    terminal = "$"
                set[terminal] = ('', [])
            self.table[non_terminal] = set

    def create_table(self):
        for non_terminal in self.grammar.productions:
            first = self.parser.FIRST[non_terminal]
            for element in first:
                production = self.check_production(non_terminal, element)
                if element == '@':
                    self.handle_epsilon(non_terminal, production)
                else:
                    self.table[non_terminal][element] = production

    def check_production(self, non_terminal, first_element):
        productions = self.grammar.productions[non_terminal]
        for p in productions:
            if first_element in p:
                return self.split_productions(non_terminal, p)
        return self.split_productions(non_terminal, productions[0])

    def handle_epsilon(self, non_terminal, production):
        follow = self.parser.FOLLOW[non_terminal]
        for element in follow:
            self.table[non_terminal][element] = production

    def split_productions(self, non_terminal, production):
        array = []
        for element in production:
            array.append(element)
        return (non_terminal, array)

    def pretty_print(self):
        print("PRODUCTIONS")
        for key in self.grammar.productions:
            print(f"{key}: {self.grammar.productions[key]}")
        print("")
        print("FIRST")
        for key in self.parser.FIRST:
            if key in self.grammar.non_terminals:
                print(f"{key}: {self.parser.FIRST[key]}")
        print("")
        print("FOLLOW")
        for key in self.parser.FIRST:
            if key in self.grammar.non_terminals:
                print(f"{key}: {self.parser.FOLLOW[key]}")
        print("")
        print("TABLE")
        for key in self.table.keys():
            print(f"{key}: {self.table[key]}")

    def check_input(self, input):
        self.init_stack()
        self.init_input_stack(input)
        flag = True
        action = []
        while flag:
            print(f"Stack: {self.stack} | i/o:{self.input}")
            element = self.stack.pop()
            input_element = self.input[-1]
            if element == '$':
                if self.input[0] == '$':
                    flag = False
                    print("Accepted")
                    action.append("accepted")
                else:
                    action.append("rejected")
                    return False
            elif element == input_element:
                self.pop()
                action.append(("pop", element))
            else:
                production = copy.deepcopy(self.table[element][input_element])
                if production[1][0] == "@":
                    pass
                    action.append(production)
                else:
                    p = copy.deepcopy(production)
                    action.append(p)
                    while len(production[1]) != 0:
                        self.stack.append(production[1].pop())
        print("---------------------------------------------")
        for a in action:
            print(a)
        print("---------------------------------------------")
        self.create_parse_tree(action)

    def printParseTree(self):
        for node in self.NODES:
            print(node)

    def create_parse_tree(self, action):
        self.parseTree = Node(action, None, self.NODES)
        self.parseTree.configure()

    def pop(self):
        self.input.pop()

    def init_stack(self):
        self.stack = []
        self.stack.append('$')
        self.stack.append(self.grammar.starting_symbol[0])

    def init_input_stack(self, input):
        self.input.append('$')
        for element in input:
            self.input.append(element)


directory_path = "/home/emanuelignat/uni-manu/compilers/FLCD/#Lab5 - Week 8/"
g = Grammar(f'{directory_path}lab_inputs/g2.json')
p = Parser(g)
p1 = ParseTable(p)
# p1.pretty_print()
p1.check_input('c:a')
p1.printParseTree()
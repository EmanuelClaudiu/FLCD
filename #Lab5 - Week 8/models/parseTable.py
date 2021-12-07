from parser import Parser
from grammar import Grammar

class ParseTable:

    def __init__(self, parser):
        self.parser = parser
        self.grammar = self.parser.grammar
        self.table = {}
        self.init_table()
        self.create_table()

    def init_table(self):
        for non_terminal in self.grammar.non_terminals:
            set = {}
            for terminal in self.grammar.terminals:
                # E[id] = E -> ab@
                if terminal == "@":
                    terminal = "$"
                set[terminal] = ('', [])
            self.table[non_terminal] = set

    def create_table(self):
        for non_terminal in self.grammar.productions:
            first = self.parser.FIRST[non_terminal]
            for element in first:
                # check epsilon !!
                production = self.check_production(non_terminal, element)
                self.table[non_terminal][element] = production

    def check_production(self, non_terminal, first_element):
        productions = self.grammar.productions[non_terminal]
        for p in productions:
            if first_element in p:
                return self.split_productions(non_terminal, p)
        return self.split_productions(non_terminal, productions[0])

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


directory_path = "/home/emanuelignat/uni-manu/compilers/FLCD/#Lab5 - Week 8/"
g = Grammar(f'{directory_path}inputs/g4.json')
p = Parser(g)
p1 = ParseTable(p)
p1.pretty_print()
import json


class Grammar:

    def __init__(self, inputFile):
        self.input_file = open(inputFile)
        self.grammar = json.load(self.input_file)
        self.non_terminals = self.grammar['non-terminals']
        self.terminals = self.grammar['terminals']
        self.productions = self.grammar['productions']
        self.starting_symbol = self.grammar['starting_symbol']

    def showMenu(self):
        flag = True
        while flag:
            print("--------------------------------------------")
            print("1.Print set of nonterminals")
            print("2.Print set of terminals")
            print("3.Print set of productions")
            print("4.Print a production for a given nonterminal")
            print("5.Check CFG")
            print("0.exit")
            print("--------------------------------------------")
            choice = input('>>')
            if choice == '0':
                flag = False
            elif choice == '1':
                print(self.non_terminals)
            elif choice == '2':
                print(self.terminals)
            elif choice == '3':
                print(self.productions)
            elif choice == '4':
                print("Pick a nonterminal from the list:")
                print(self.non_terminals)
                choice = input(">>")
                try:
                    productions = self.productions[choice]
                    toPrint = str(choice) + " -> "
                    for production in productions:
                        toPrint += str(production) + " | "
                    print(toPrint)
                except KeyError:
                    print("Can't find provided nonterminal")
            elif choice == '5':
                productions = self.productions
                keys = [key for key in productions.keys()]
                try:
                    for key in keys:
                        if not self.checkIfNonterminal(key):
                            raise BaseException
                        for value in productions[key]:
                            for character in value:
                                if not self.checkIfNonterminal(character) and not self.checkIfTerminal(character):
                                    raise BaseException
                    print("Grammar is context free")
                except BaseException:
                    print("Grammar is not context free")

    def checkIfNonterminal(self, character):
        if character in self.non_terminals:
            return True
        return False

    def checkIfTerminal(self, character):
        if character in self.terminals:
            return True
        return False

directory_path = "/home/emanuelignat/uni-manu/compilers/FLCD/#Lab5 - Week 8/"
g = Grammar(f'{directory_path}inputs/g1.json')
g.showMenu()
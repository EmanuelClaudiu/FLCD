from grammar import Grammar

class Parser:

    def __init__(self, grammar):
        self.grammar = grammar

    def compute_FIRST_set(self, symbol):
        # take first terminal symbols from derived strings
        toReturn = []
        if symbol not in self.grammar.non_terminals and symbol not in self.grammar.terminals:
            #character is not part of alphabet
            return toReturn
        if symbol in self.grammar.terminals:
            # symbol is terminal
            return [symbol]
        #symbol is non terminal
        for string in self.grammar.productions[symbol]:
            for character in string:
                if self.grammar.checkIfTerminal(character):
                    if character not in toReturn:
                        toReturn.append(character)
                    break
        return toReturn

    def compute_FOLLOW_set(self):
        # take terminal symbols immediately to the right
        pass



directory_path = "/home/emanuelignat/uni-manu/compilers/FLCD/#Lab5 - Week 8/"
g = Grammar(f'{directory_path}inputs/g1.json')
p = Parser(g)
print(p.compute_FIRST_set("A"))
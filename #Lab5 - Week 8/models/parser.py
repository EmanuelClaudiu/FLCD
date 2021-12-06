from grammar import Grammar

class Parser:

    def __init__(self, grammar):
        self.grammar = grammar
        self.FIRST = {}
        self.FOLLOW = {}
        self.compute_FIRST()
        self.compute_FOLLOW()

    def compute_FIRST(self):
        terminals = self.grammar.terminals
        non_terminals = self.grammar.non_terminals
        productions = self.grammar.productions
        F = []
        i = 0
        # initialization (construct F0)
        F0 = {}
        for a in terminals:
            F0_a = [a]
            F0[a] = F0_a
        for A in non_terminals:
            F0_A = []
            for production in productions[A]:
                if self.grammar.checkIfTerminal(production[0]):
                    F0_A.append(production[0])
            F0[A] = F0_A
        F.append(F0)
        flag = True
        while flag:
            i = i + 1
            Fi = {}
            for A in non_terminals:
                Fi_A = []
                lastF_A = F[i-1][A]
                Fi_A += lastF_A
                for production in productions[A]:
                    if len(F[i - 1][production[0]]) == 0:
                        Fi_A = self.concatenate_lists(Fi_A, [])
                    else:
                        concatenation_terms = [F[i-1][term] for term in production]
                        Fi_A = self.concatenate_lists(
                            Fi_A,
                            self.concatenation(concatenation_terms)
                        )
                Fi[A] = Fi_A
            for a in terminals:
                Fi_a = [a]
                Fi[a] = Fi_a
            F.append(Fi)
            flag = False
            for key in F[i].keys():
                if not self.areListsEqual(F[i][key], F[i-1][key]):
                    flag = True
        self.FIRST = F[-1]
        return F[-1]

    def compute_FOLLOW(self):
        # take terminal symbols immediately to the right
        terminals = self.grammar.terminals
        non_terminals = self.grammar.non_terminals
        productions = self.grammar.productions
        L = []
        # initialization (compute L0)
        L0 = {}
        for non_terminal in non_terminals:
            if non_terminal == self.grammar.starting_symbol[0]:
                L0[non_terminal] = ['$']
            else:
                L0[non_terminal] = []
        L.append(L0)
        i = 0
        flag = True
        while flag:
            i = i + 1
            Li = {}
            for B in non_terminals:
                Li_B = []
                occurencies = self.get_occurencies(B)
                y_list = []
                for occurency in occurencies:
                    y_list.append((occurency[0], self.get_next_term(B, occurency)))
                for x in y_list:
                    y = x[1]
                    A = x[0]
                    if y != '':
                        first_y = self.FIRST[y]
                        for a in first_y:
                            if a == '@':
                                Li_B = self.concatenate_lists(Li_B, Li_B)
                                Li_B = self.concatenate_lists(Li_B, L[i - 1][A])
                            else:
                                Li_B = self.concatenate_lists(Li_B, L[i - 1][B])
                                Li_B = self.concatenate_lists(Li_B, first_y)
                                Li_B = list(filter(lambda x: x != '@', Li_B))
                    else:
                        Li_B = self.concatenate_lists(Li_B, L[i - 1][B])
                        Li_B = self.concatenate_lists(Li_B, L[i - 1][A])
                Li[B] = Li_B
            L.append(Li)
            flag = False
            for key in L[i].keys():
                if not self.areListsEqual(L[i][key], L[i - 1][key]):
                    flag = True
        self.FOLLOW = L[-1]
        return L[-1]

    def get_occurencies(self, B):
        occurencies = []
        for key in self.grammar.productions.keys():
            for production in self.grammar.productions[key]:
                if B in production:
                    occurencies.append((key, production))
        return occurencies

    def get_next_term(self, B, occurency):
        production = occurency[1]
        if B == production[-1]:
            return ''
        for i in range(0, len(production)):
            if production[i] == B:
                return production[i + 1]

    def concatenation(self, concatenation_terms):
        if [] in concatenation_terms:
            return []
        if '@' in concatenation_terms[0]:
            toReturn = []
            for term in concatenation_terms:
                toReturn += term
            # remove epsilon
            toReturn = list(filter(lambda x: x != '@', toReturn))
            return toReturn
        if len(concatenation_terms[0]) == 0:
            return []
        else:
            return concatenation_terms[0]

    def concatenate_lists(self, listA, listB):
        toReturn = []
        for item in listA:
            if item not in toReturn:
                toReturn.append(item)
        for item in listB:
            if item not in toReturn:
                toReturn.append(item)
        return toReturn

    def areListsEqual(self, listA, listB):
        if len(listA) != len(listB):
            return False
        for item in listA:
            if item not in listB:
                return False
        return True

directory_path = "/home/emanuelignat/uni-manu/compilers/FLCD/#Lab5 - Week 8/"
g = Grammar(f'{directory_path}inputs/g4.json')
p = Parser(g)
print(p.grammar)
print(p.FIRST)
print(p.FOLLOW)
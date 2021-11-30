from grammar import Grammar

class Parser:

    def __init__(self, grammar):
        self.grammar = grammar

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
        return F[-1]

    def compute_FOLLOW(self):
        # take terminal symbols immediately to the right
        pass

    def concatenation(self, concatenation_terms):
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
g = Grammar(f'{directory_path}inputs/g3.json')
p = Parser(g)
F_set = print(p.compute_FIRST())
import json

DIRECTORY_PATH = "/home/emanuelignat/uni-manu/compilers/FLCD/Lab6/"
INPUT_FILE = DIRECTORY_PATH + "FA.json"

class FiniteAutomaton:
    
    def __init__(self, inputFile):
        self.FA = json.load(open(inputFile, "r"))
        
    def __str__(self):
        return f'{self.FA}'
    
    def showElements(self):
        flag = True
        while flag:
            print('----------------------------')
            print('0.exit')
            print('1.Print set of all states')
            print('2.Print the alphabet')
            print('3.Print transition functions')
            print('4.Print set of final states')
            print('----------------------------')
            choice = input('>>')
            if choice == '0':
                flag = False
            elif choice == '1':
                print(self.FA["set of states"])
            elif choice == '2':
                print(self.FA["alphabet"])
            elif choice == '3':
                print(self.FA["transition function"])
            elif choice == '4':
                print(self.FA["set of final states"])
                
    def checkIfAccepted(self, sequence):
        current_state = self.FA["start state"]
        transitions = self.FA["transition function"]
        for element in sequence:
            current_state = transitions[current_state][element]
        if current_state in self.FA["set of final states"]:
            return True
        return False

fa = FiniteAutomaton(INPUT_FILE)
fa.showElements()

'''
# should accept
print(fa.checkIfAccepted(["1", "1", "1"]))
# should accept
print(fa.checkIfAccepted(["0", "1", "1", "1", "1", "1"]))
# should not accept
print(fa.checkIfAccepted(["1"]))
# should not accept
print(fa.checkIfAccepted(["0", "1"]))
'''
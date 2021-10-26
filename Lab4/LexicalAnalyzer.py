from  ST.symbol_table import SymbolTable
import re
from enum import Enum
from operator import itemgetter
from tokens.regular_expressions import operator_re, whitespace_re, reserved_word_re, identifier_re, constant_re
import os

class LexicalType(Enum):
    RESERVED_WORD = 0
    OPERATOR = 1
    SEPARATOR = 2
    IDENTIFIER = 3
    CONSTANT = 4
    COMMENT = 5
    ERROR = 6
class LexicalAnalyzer():

    def __init__(self, symbol_table):
        self.program = None
        self.ST = symbol_table
        self.PIF = []
        self.comment_active = False
        self.operator_regex = operator_re
        self.separator_regex = whitespace_re
        self.reserved_word_regex = reserved_word_re
        self.identifier_regex = identifier_re
        self.constant_regex = constant_re
        self.errors = []

    def genPIF(self, token, index=0):
        if index == -1:
            # token is reserved_word / operator / separator
            self.PIF.append((token, -1))
            self.ST.insert(token, -1)
        else:
            # token is identifier / constant
            if len(self.PIF) == 0:
                # PIF is empty
                self.PIF.append((token, 0))
                self.ST.insert(token, 0)
            else:
                # PIF is not empty
                max_index = max(self.PIF,key=itemgetter(1))[1]
                response = self.ST.insert(token, max_index + 1)
                if response != None:
                    self.PIF.append((token, response))
                else:
                    self.PIF.append((token, max_index + 1))

    def detect(self, token):
        #special case
        if token == '':
            return LexicalType.SEPARATOR
        # check if comment
        if token == '-comment-':
            self.comment_active = True
            return LexicalType.RESERVED_WORD
        elif token == '-/comment-':
            self.comment_active = False
            return LexicalType.RESERVED_WORD

        if not self.comment_active:
            # check if operator
            if re.search(self.operator_regex, token):
                return LexicalType.OPERATOR
            # check if separator
            elif re.search(self.separator_regex, token):
                return LexicalType.SEPARATOR
            # check if reserved word
            elif re.search(self.reserved_word_regex, token):
                return LexicalType.RESERVED_WORD
            # check if identifier
            elif re.search(self.identifier_regex, token):
                return LexicalType.IDENTIFIER
            # check if constant (integer, boolean, string, float, void)
            elif re.search(self.constant_regex, token):
                return LexicalType.CONSTANT
            else:
                return LexicalType.ERROR
        return LexicalType.COMMENT
        
    def parse_token(self, token):
        lexical_type = self.detect(token)
        if lexical_type == LexicalType.RESERVED_WORD or lexical_type == LexicalType.OPERATOR or lexical_type == LexicalType.SEPARATOR:
            # add to ST with index -1
            self.genPIF(token, -1)
            return {"message": "ok"}
        elif lexical_type == LexicalType.IDENTIFIER or lexical_type == LexicalType.CONSTANT:
            # add to ST with index
            self.genPIF(token)
            return {"message": "ok"}
        elif lexical_type == LexicalType.COMMENT:
            # is inside a comment, we ignore it
            return {"message": "ok"}
        else:
            # lexical error
            return {"message": "Lexical error"}

    def parse_line(self, line):
        tokens = line.split(' ')
        for token in tokens:
            if "\n" in token:
                # trim the newline off the token
                token = token[:-1]
            response = self.parse_token(token)
            if response["message"] != "ok":
                self.errors.append(f"Lexical error at token: {token}")

    def parse_file(self):
        # opens the program file and reads through it line by line
        with open(self.program, 'r') as file:
            line = file.readline()
            while line:
                self.parse_line(line)
                line = file.readline()
                
    def run(self, programFile):
        self.program = programFile
        self.parse_file()
        if len(self.errors) == 0:
            for element in self.PIF:
                print(element)
            print(self.ST)
        else:
            for error in self.errors:
                print(error)

directory_path = "/home/emanuelignat/uni-manu/compilers/FLCD/Lab4/"
p1 = directory_path + "programs/p1.txt"
p1_err = directory_path + "programs/p1err.txt"
p2 = directory_path + "programs/p2.txt"
p3 = directory_path + "programs/p3.txt"

st = SymbolTable()
l = LexicalAnalyzer(st)
l.run(p1_err)

# TODO: integer can be negative, PIF index should be position from ST
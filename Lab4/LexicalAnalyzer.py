from  ST.symbol_table import SymbolTable
import re
from enum import Enum
from tokens.regular_expressions import operator_re, whitespace_re, reserved_word_re, identifier_re, constant_re
import os

class LexicalType(Enum):
    RESERVED_WORD = 0
    OPERATOR = 1
    SEPARATOR = 2
    IDENTIFIER = 3
    CONSTANT = 4
    ERROR = 5
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
        
    def parse_token(self, token):
        lexical_type = self.detect(token)
        if lexical_type == LexicalType.RESERVED_WORD or lexical_type == LexicalType.OPERATOR or lexical_type == LexicalType.SEPARATOR:
            # add to ST with index -1
            pass
        elif lexical_type == LexicalType.IDENTIFIER or lexical_type == LexicalType.CONSTANT:
            # add to ST with index
            pass
        else:
            # lexical error
            pass

    def parse_line(self, line):
        tokens = line.split(' ')
        for token in tokens:
            print('--------------------------------')
            print(f'{token} -> {self.detect(token)}')
            print('--------------------------------')
        for token in tokens:
            self.parse_token(token)

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


directory_path = "/home/emanuelignat/uni-manu/compilers/FLCD/Lab4/"
p1 = directory_path + "programs/p1.txt"
p1_err = directory_path + "programs/p1err.txt"
p2 = directory_path + "programs/p2.txt"
p3 = directory_path + "programs/p3.txt"

st = SymbolTable()
l = LexicalAnalyzer(st)
l.run(p1)
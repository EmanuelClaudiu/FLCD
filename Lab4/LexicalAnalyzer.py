from  ST.symbol_table import SymbolTable
import re
from tokens.regular_expressions import operator_re, whitespace_re, reserved_word_re, identifier_re, constant_re
import os

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
        # check if comment
            if '/' in token:
                self.comment_active = False
            else:
                self.comment_active = True
        # check if operator
        # check if separator
        # check if reserved word
        # check if identifier
        # check if constant (integer, boolean, string, float, void)
        

    def parse_line(self, line):
        tokens = line.split(' ')
        for token in tokens:
            self.detect(token)

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
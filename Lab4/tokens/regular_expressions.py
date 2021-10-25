import re

operator_re = re.compile(r'^[+*/%=:!><-]$|^[=!]=$|^[+]{2}$|^[-]{2}$|^[+-]=$|^[<>]=$')
whitespace_re = re.compile(r'^\s$|^[\(\)\[\]]$')
reserved_word_re = re.compile(
    r'^skip$|' 
    + r'^/?if$|'
    + r'^else$|'
    + r'^/ifelse$|'
    + r'^integer$|'
    + r'^boolean$|'
    + r'^string$|'
    + r'^float$|'
    + r'^void$|'
    + r'^[-]/?comment[-]$|'
    + r'^return$|'
    + r'^/?from$|'
    + r'^to$|'
    + r'^as$|'
    + r'^/?while$|'
    + r'^read_integer$|'
    + r'^read_float$|'
    + r'^read_boolean$|'
    + r'^read_string$|'
    + r'^print$'
)
identifier_re = re.compile(r'^[_]*[a-zA-Z0-9\_]+$')
constant_re = re.compile(
    r'^[0-9]$|^[1-9][0-9]+$|'
    + r'^true$|^false$|'
    + r'^[\'].*[\']$|^[\"].*[\"]$|'
    + r'^[0-9][.][0-9]+$|^[1-9][0-9]+[.][0-9]+$'
)
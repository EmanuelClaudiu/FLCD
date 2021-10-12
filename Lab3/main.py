from binary_search_tree import BinarySearchTree
from symbol_table import SymbolTable

symbol_table = SymbolTable()

print(str(symbol_table.insert('c', 0)))
print(str(symbol_table.insert('b', 1)))
print(str(symbol_table.insert('a', 2)))
print(str(symbol_table.insert('e', 3)))
print(str(symbol_table.insert('d', 4)))

print(str(symbol_table.insert('c', 5)))

print(str(symbol_table))
print(str(symbol_table.get('d')))
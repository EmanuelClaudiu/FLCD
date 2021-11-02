import json

directory_path = "/home/emanuelignat/uni-manu/compilers/FLCD/Lab6/"
input_file = directory_path + "FA.json"
file = open(input_file, "r")
print(json.load(file))
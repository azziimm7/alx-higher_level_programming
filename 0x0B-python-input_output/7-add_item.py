#!/usr/bin/python3

"""This module contains a script that Deserialize
a JSON file, append to its content, and save the result"""


from json import load
from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

my_args = argv[1:]
try:
    my_list = load_from_json_file("add_item.json")
except FileNotFoundError:
    my_list = []

for arg in my_args:
    my_list.append(arg)

save_to_json_file(my_list, "add_item.json")

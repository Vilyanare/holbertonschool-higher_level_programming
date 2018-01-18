#!/usr/bin/python3
"""Adds command line arguments to file encoded with JSON"""
import sys
save = __import__('7-save_to_json_file').save_to_json_file
load = __import__('8-load_from_json_file').load_from_json_file
temp = []
try:
    temp = load('add_item.json')
except:
    pass
for i in range(1, len(sys.argv)):
    temp += [sys.argv[i]]
save(temp, 'add_item.json')

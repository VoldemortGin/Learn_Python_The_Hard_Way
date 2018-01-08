# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from sys import argv

script, filename = argv

txt = open(filename)

print("Here's your file %r:" % filename)
print(txt.read())

print("Type the filename again:")
file_again = input(">")     # Make sure the filename printed is correct.

txt_again = open(file_again)

print(txt_again.read())


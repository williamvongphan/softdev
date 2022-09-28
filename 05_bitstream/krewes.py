"""
Duo <tpng name here lol> Hui Wang, William Vongphanith
SoftDev
K05 -- Bitstream
2022-09-28
Time Spent: <t> hours
"""

import random

parsing_types = ["period", "name", "ducky"]

def next_element(array, element):
    """Returns the next element in an array"""
    return array[(array.index(element) + 1) % len(array)]

# read file
f = open("krewes.txt", "r")

# it's called bitstream so we are not going to split/split again
krewes = {}

# read file (one line) letter by letter
krewes_stream = f.read()

current_period = ""
current_name = ""
current_ducky = ""

current_character = ""
dollar_sign_count = 0
at_sign_count = 0

current_parsing_type = "period"

# Input looks like this:
# pd$$$name$$$ducky@@@anotherpd$$$anothername$$$anotherducky@@@...

for i in krewes_stream:
    if i == "$":
        dollar_sign_count += 1
        at_sign_count = 0
        current_character = "$"
    elif i == "@":
        at_sign_count += 1
        dollar_sign_count = 0
        current_character = "@"
    else:
        current_character = i
        if current_parsing_type == "period":
            current_period += current_character
        elif current_parsing_type == "name":
            current_name += current_character
        elif current_parsing_type == "ducky":
            current_ducky += current_character

    if current_character == "$" and dollar_sign_count == 3:
        dollar_sign_count = 0
        current_parsing_type = next_element(parsing_types, current_parsing_type)

    if current_character == "@" and at_sign_count == 3:
        at_sign_count = 0
        current_parsing_type = next_element(parsing_types, current_parsing_type)

        krewe_member = (current_name, current_ducky)
        # Create list of krewe members
        if current_period in krewes:
            krewes[current_period].append(krewe_member)
        else:
            krewes[current_period] = [krewe_member]

        current_period = ""
        current_name = ""
        current_ducky = ""

print(krewes)


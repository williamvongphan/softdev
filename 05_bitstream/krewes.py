"""
Duo XeraRedStar: Hui Wang, William Vongphanith
SoftDev
K05 -- Bitstream
2022-09-28
Time Spent: 0.6 hours
"""

import random

parsing_types = ["period", "name", "ducky"]

def next_element(array, element):
    """Returns the next element in an array"""
    return array[(array.index(element) + 1) % len(array)]

# read file
f = open("krewes.txt", "r")

# read file (one line) letter by letter
krewes_stream = f.read()

# Input looks like this:
# pd$$$name$$$ducky@@@anotherpd$$$anothername$$$anotherducky@@@...

def parse_stream(stream):
    krewes = {}

    current_period = ""
    current_name = ""
    current_ducky = ""
    
    current_character = ""
    dollar_sign_count = 0
    at_sign_count = 0
    
    current_parsing_type = "period"
    
    for i in stream:
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

    return krewes

# Now choose a random krewe member
def choose_krewe_member(krewes):
    period = random.choice(list(krewes.keys()))
    krewe_member = random.choice(krewes[period])
    return (period, krewe_member)

krewes = parse_stream(krewes_stream)
print("Chose " + str(choose_krewe_member(krewes)[1][0]) + " from period " + str(choose_krewe_member(krewes)[0]) + " (their ducky is " + str(choose_krewe_member(krewes)[1][1]) + ")")

"""
Our answers for Coding Bat's Python Warmup
"""

# Sleep in
def sleep_in(weekday, vacation):
  if weekday == True and vacation == False:
    return False
  else:
    return True

# Monkey Trouble
def monkey_trouble(a_smile, b_smile):
  if a_smile == b_smile:
    return True
  else:
    return False

# Sum Double
def sum_double(a, b):
    if a == b:
        return 2 * (a + b)
    else:
        return a + b

# Diff 21
def diff21(n):
    if n <= 21:
        return 21 - n
    else:
        return 2 * (n - 21)

# Parrot Trouble
def parrot_trouble(talking, hour):
    if talking == True and (hour < 7 or hour > 20):
        return True
    else:
        return False

# Makes 10
def makes10(a, b):
    if a == 10 or b == 10 or a + b == 10:
        return True
    else:
        return False

# Near 100
def near_hundred(n):
    if abs(100 - n) <= 10 or abs(200 - n) <= 10:
        return True
    else:
        return False

# Pos Neg
def pos_neg(a, b, negative):
    if negative == True:
        if a < 0 and b < 0:
            return True
        else:
            return False
    else:
        if (a < 0 and b > 0) or (a > 0 and b < 0):
            return True
        else:
            return False

# Not String
def not_string(str):
    if str[:3] == "not":
        return str
    else:
        return "not " + str

# Missing Char
def missing_char(str, n):
    return str[:n] + str[n+1:]

# Front Back
def front_back(str):
    if len(str) <= 1:
        return str
    else:
        return str[-1] + str[1:-1] + str[0]

# Front 3
def front3(str):
    if len(str) < 3:
        return str * 3
    else:
        return str[:3] * 3

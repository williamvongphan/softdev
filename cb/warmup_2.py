"""
Our answers for Coding Bat's Python Warmup 2
"""

# String Times
def string_times(str, n):
    return str * n

# Front Times
def front_times(str, n):
    return str[:3] * n

# String Bits
def string_bits(str):
    return str[::2]

# String Splosion
def string_splosion(str):
    i = 0
    new_str = ''
    while i < len(str):
        new_str += str[:i+1]
        i += 1
    return new_str

# Last 2
def last2(str):
    if len(str) < 2:
        return 0
    last2 = str[-2:]
    count = 0
    for i in range(len(str)-2):
        sub = str[i:i+2]
        if sub == last2:
            count += 1
    return count

# Array Count 9
def array_count9(nums):
    count = 0
    for num in nums:
        if num == 9:
            count += 1
    return count

# Array Front 9
def array_front9(nums):
    for num in nums[:4]:
        if num == 9:
            return True
    return False

# Array 123
def array123(nums):
    for i in range(len(nums)-2):
        if nums[i:i+3] == [1, 2, 3]:
            return True
    return False

# String Match
def string_match(a, b):
    count = 0
    for i in range(min(len(a), len(b))-1):
        if a[i:i+2] == b[i:i+2]:
            count += 1
    return count

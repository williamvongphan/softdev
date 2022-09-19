"""
Codingbat List-1 has23
"""
def has23(nums):
    """
    Given an int array length 2, return True if it contains a 2 or a 3.
    """
    return 2 in nums or 3 in nums

def main():
    """
    Main function
    """
    print(has23([2, 5]))
    print(has23([4, 3]))
    print(has23([4, 5]))

if __name__ == "__main__":
    main()

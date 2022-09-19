"""
Codingbat List-2 has22
"""

def has22(nums):
    """
    Given an array of ints, return True if the array contains a 2 next to a 2
    somewhere.
    """
    for i in range(len(nums)-1):
        if nums[i] == 2 and nums[i+1] == 2:
            return True
    return False

def main():
    """
    Main function
    """
    print(has22([1, 2, 2]))
    print(has22([1, 2, 1, 2]))
    print(has22([2, 1, 2]))

if __name__ == "__main__":
    main()

"""
Codingbat Warmup-1 pos_neg
"""
def pos_neg(a, b, negative):
    """
    Given 2 int values, return True if one is negative and one is positive.
    Except if the parameter "negative" is True, then return True only if both
    are negative.
    """
    if negative:
        return a < 0 and b < 0
    return (a < 0 and b > 0) or (a > 0 and b < 0)

if __name__ == "__main__":
    print(pos_neg(1, -1, False))
    print(pos_neg(-1, 1, False))
    print(pos_neg(-4, -5, True))

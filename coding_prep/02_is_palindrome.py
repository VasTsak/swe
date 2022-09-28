"""
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

For example, 121 is a palindrome while 123 is not.
"""

def is_palindrome(x: int) -> bool:
    """
    Given an integer return whether it is a palindrome or not.
    Arguments:
        x: int
            Integer to be tested whether it is palindrome.
    Return:
        result: bool
            Condition whether it is a palindrome or not.
    """
    x = str(x)
    if len(x) < 2:
        return True
    for i in range(len(x)//2):
        if x[i] != x[-(i+1)]:
            return False
    return True


def main():
    # Test 1
    t1 = is_palindrome(121)
    assert t1, "Wrong value."
    # Test 2
    t2 = is_palindrome(1234)
    assert t2==False, "Wrong value."
    # Test 3
    t3 = is_palindrome(1)
    assert t3, "Wrong value."
    # Test 4
    t4 = is_palindrome(123321)
    assert t4, "Wrong value."

if __name__ == "__main__":
    main()
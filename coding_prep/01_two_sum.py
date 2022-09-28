"""
Given an array of integers nums and an integer target, return indices of the two numbers 
such that they add up to target.

You may assume that each input would have exactly one solution, and you may not 
use the same element twice.

You can return the answer in any order.
"""

def two_sum(nums: list, target: float) -> list:
    """
    Return the indexes of the two numbers which sum up to a target number

    Arguments:
        nums: list
            List of numbers used to sum up of the target number
        target: float
            Number which is the sum of two elements. 
    Return: 
        l: list
            List of indexes of the numbers used to calculate the sum
    """

    hashmap = {}
    l = []
    for i in range(len(nums)):
        difference = target - nums[i]
        if nums[i] in hashmap.keys():
            l = [hashmap[nums[i]], i]
            return l
        hashmap[difference] = i

    return l


def main():

    # Test 1
    t1 = two_sum([1, 2, 3, 4], 4)
    assert t1 == [0, 2], "Wrong indexes."

    # Test 2
    t2 = two_sum([-5, 2, 4, 8, 19, 10000], -1)
    assert t2 == [0, 2], "Wrong indexes."

    # Test 3
    try: 
        t3 = 

if __name__ == "__main__":
    main()
#!/usr/bin/env python3.13
"""
Given an integer array [nums] of size n, return the number with the value
closest to in [nums]. If there are multiple answers, return the number
with the largest value.
"""
from typing import List


class Solution:
    """
    Solution: Example
    Input: nums = [-4, -2, 1, 4, 8]
    Ouput: 1
    Explanation:
        The distance from -4 to 0 is |-4| = 4.
        The distance from -4 to 0 is |-2| = 2.
        The distance from -4 to 0 is |1| = 1.
        The distance from -4 to 0 is |4| = 4.
        The distance from -4 to 0 is |8| = 8.
    Thus, the closest number to 0 in [nums] is 1.
    """
    def findClosestNumber(self, nums: List[int]) -> int:
        """
        """
        ans: int = nums[0]

        for num in nums:
            # compare absolute values
            if abs(num) < abs(ans):
                ans = num
            # if absolute values are equal, choose the positive one
            elif abs(num) == abs(ans) and num > ans:
                ans = num
        return ans

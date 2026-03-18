"""
You are given a binary array [nums], return the maximun number of consecutive 1´s in the array. 

Example 1: 

Input: nums = [1, 1, 0, 1, 1, 1]

Output: 3

Example 2: 

Input: nums = [1, 0, 1, 1, 0, 1]

Output: 2

Constraints: 

- 1<= nums.lenght <= 100,000
- nums[i] is either 0 or 1. 

"""

class Solution: 
    def findMaxConsecutivesOnes(self, nums: List[int]) -> int: 
        con = mx = 0
        for i in nums: 
            if i == 1: 
                con += 1
            else: 
                con = 0
            mx = max(mx, con)
        return mx
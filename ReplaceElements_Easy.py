"""
Replace Elements With Greatest Element On Right Side

You are given an array [arr], replace every elemet in that array with the greatest element
among the elements to its right, and replace the last element with [-1]- 

After doing so, return the array. 

Example 1: 

Input: arr = [2, 4, 5, 3, 1, 2]

Output: [5, 5, 3, 2, 2, -1]

Example 2: 

Input: arr = [3, 3]

Output: [3, -1]

"""

class Solution: 
    def replaceElements(self, arr: List[int]) -> List[int]:
        fin = -1
        n = len(arr)
        for i in range(n - 1, -1, -1):
            temp = arr[i]
            arr[i] = fin
            fin = max(fin, temp)
        return arr
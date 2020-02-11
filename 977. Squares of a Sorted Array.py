'''
easy

Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.
'''

class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        a_sqr = [i**2 for i in A]
        a_sqr.sort()
        return a_sqr


class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        
        return sorted([i**2 for i in A])
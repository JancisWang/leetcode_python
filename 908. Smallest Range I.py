'''
easy

Given an array A of integers, for each integer A[i] we may choose any x with -K <= x <= K, and add x to A[i].

After this process, we have some array B.

Return the smallest possible difference between the maximum value of B and the minimum value of B.
'''

class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        max_v = max(A)
        min_v = min(A)
        if max_v - min_v <= 2 * K: return 0
        return max_v - min_v - 2*K
    
        
class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        return max(0, max(A) - min(A) - 2*K)
       

class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        A.sort()

        if A[-1] - A[0] <= 2 * K: return 0
        return A[-1] - A[0] - 2*K